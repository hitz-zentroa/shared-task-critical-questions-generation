import json
from transformers import AutoTokenizer, LlamaForCausalLM, GenerationConfig
import logging
import tqdm
import re

logging.basicConfig()
logger = logging.getLogger()

def output_cqs(model_name, text, prefix, model, tokenizer, new_params, remove_instruction=False):

    instruction = prefix.format(**{'intervention':text})

    inputs = tokenizer(instruction, return_tensors="pt")
    inputs = inputs.to('cuda')

    if new_params:
        outputs = model.generate(**inputs, **new_params) 
    else:
        outputs = model.generate(**inputs)

    out = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

    if remove_instruction:
        try:
            out = out.split('<|assistant|>')[1]
        except IndexError:
            out = out[len(instruction):]

    return out

def structure_output(whole_text):
    cqs_list = whole_text.split('\n')
    final = []
    valid = []
    not_valid = []
    for cq in cqs_list:
        if re.match('.*\?(\")?( )?(\([a-zA-Z0-9\.\'\-,\? ]*\))?([a-zA-Z \.,\"\']*)?(\")?$', cq):
            valid.append(cq)
        else:
            not_valid.append(cq)

    still_not_valid = []
    for text in not_valid:
        new_cqs = re.split("\?\"", text+'end')
        if len(new_cqs) > 1:
            for cq in new_cqs[:-1]:
                valid.append(cq+'?\"')
        else:
            still_not_valid.append(text)

    for i, cq in enumerate(valid):
        occurrence = re.search(r'[A-Z]', cq)
        if occurrence:
            final.append(cq[occurrence.start():])
        else:
            continue

    output = []
    if len(final) >= 3:
        for i in [0, 1, 2]:
            output.append({'id':i, 'cq':final[i]})
        return output
    else:
        logger.warning('Missing CQs')
        return 'Missing CQs'


def main():

    prefixes = ["""Suggest 3 critical questions that should be raised before accepting the arguments in this text:
                
                "{intervention}"
                
                Give one question per line. Make the questions simple, and do not give any explanation reagrding why the question is relevant."""]
    
    with open('shared_task/data_splits/sample.json') as f:
        data=json.load(f)

    models = ['meta-llama/Meta-Llama-3-8B-Instruct'] 

    out = {}
    for model_name in models:
        new_params = False
        logger.info(model_name)
        generation_config = GenerationConfig.from_pretrained(model_name)
        logger.info(generation_config)
        
        model = LlamaForCausalLM.from_pretrained(model_name, device_map="auto")
        remove_instruction = True
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        logger.info('Loaded '+model_name)
        for key,line in tqdm.tqdm(data.items()):
            for prefix in prefixes:
                text = line['intervention']
                cqs = output_cqs(model_name, text, prefix, model, tokenizer, new_params, remove_instruction)
                line['cqs'] = structure_output(cqs)
                out[line['intervention_id']]=line

    with open('shared_task/trial_submission/output_llama8.json', 'w') as o:
        json.dump(out, o, indent=4)

if __name__ == "__main__":
        main()