#!/bin/bash

python shared_task/trial_submission/generate.py

python shared_task/eval_scripts/evaluation.py \
    --metric similarity \
    --input_path shared_task/data_splits/sample.json \
    --submission_path shared_task/trial_submission/output_llama8.json \
    --threshold 0.6 