#!/usr/bin/sh

./hadoop_mapper.py matrix.json  | sort | ./hadoop_reducer.py > result_matrix.txt
