#! /usr/bin/env bash

INPUT_NAME=train
OUTPUT_NAME=train-modified

date
python train.py -s input/$INPUT_NAME -m output/$OUTPUT_NAME --eval && \
python render.py -m output/$OUTPUT_NAME && \
python metrics.py -m output/$OUTPUT_NAME
date
