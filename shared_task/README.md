### Critical Questions Generation

## Setup

To run the scripts, please install the requirements.

```
pip install -r requirements.txt
```

## Run the trial submission

A simple baseline has been release in ```trial_submission```. To run and evaluate it, follow this command (you will need a GPU):

```
cd ..
sh trial_submission/run.sh 
```

## Evaluate your submissions

To evaluate your own submissions, run the following script:

```
cd ..
python shared_task/eval_scripts/evaluation.py \
    --metric similarity \
    --input_path shared_task/data_splits/sample.json \ # change this to validation for development
    --submission_path $PATH_TO_YOUR_SUBMISSION \
    --threshold 0.6 
```
