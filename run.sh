#!/bin/bash

python3 filter_ages.py
echo "state"
python3 make_population.py
echo "state"
python3 analyze.py