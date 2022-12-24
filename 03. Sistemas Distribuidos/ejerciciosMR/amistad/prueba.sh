#!/usr/bin/sh

./hadoop_mapper.py friends.json | sort | ./hadoop_reducer.py > results_friends.txt
