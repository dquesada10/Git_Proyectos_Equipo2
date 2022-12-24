#!/usr/bin/env python3
"""A more advanced Reducer, using Python iterators and generators."""
 
from itertools import groupby
from operator import itemgetter
import sys
 
def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)
 
def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["<current_word>", "<count>"] items
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            if (total_count == 0):
                # La condición sirve para descartar las simétricas
                l=str(current_word).split("_")
                print ("%s%s%s" % (l[0],separator,l[1]))

        except ValueError:
            #count was not a number
            pass

if __name__ == "__main__":
   main()
