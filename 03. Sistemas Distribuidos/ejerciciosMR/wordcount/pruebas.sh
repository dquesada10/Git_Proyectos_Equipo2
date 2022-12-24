#!/usr/bin/sh

cat amanecer.txt | ./mapper.py 
cat amanecer.txt | ./mapper.py | sort
cat amanecer.txt | ./mapper.py | sort | ./reducer.py 
cat sherlock.txt | ./mapper.py | sort | ./reducer.py 
cat sherlock.txt | ./mapper.py | sort | ./reducer.py  > result_sherlock.txt
cat quijote.txt | ./mapper.py | sort | ./reducer.py  > result_quijote.txt
cat amanecer.txt | ./hadoop_mapper.py | sort | ./hadoop_reducer.py
cat sherlock.txt | ./hadoop_mapper.py | sort | ./hadoop_reducer.py  > result_hadoop_sherlock.tx
cat quijote.txt | ./hadoop_mapper.py | sort | ./hadoop_reducer.py  > result_hadoop_quijote.txt
