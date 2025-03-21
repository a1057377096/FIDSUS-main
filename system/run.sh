#!/bin/bash

source D:/devSoft/anaconda3/etc/profile.d/conda.sh
conda activate fl
set -ex

algos=("FedAvg")
datasets=("NSLKDD")
jr="1"
client_activity_rate="0"
batch_size="64"
num_clients=10
num_classes=10
for algo in "${algos[@]}"; do
    for dataset in "${datasets[@]}"; do
        go_value="_nc${num_clients}"
        python main.py -algo "$algo" -jr "$jr" -data "$dataset" -go "$go_value" -nc "$num_clients" \
                       -nb "$num_classes" -car "$client_activity_rate" -lbs "$batch_size"
    done
done