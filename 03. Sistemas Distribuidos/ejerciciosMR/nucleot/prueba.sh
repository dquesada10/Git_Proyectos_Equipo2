#!/usr/bin/sh

./hadoop_mapper.py dna.json | sort | ./hadoop_reducer.py > results_nucleot.txt
