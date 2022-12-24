#!/usr/bin/sh

./hadoop_mapper.py books.json | sort -k 1,1 | ./hadoop_reducer.py > results_books.txt
