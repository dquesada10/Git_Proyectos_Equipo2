#!/usr/bin/env python3
"""A more advanced Reducer, using Python iterators and generators."""
 
from itertools import groupby
# from operator import itemgetter
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
    #   iter - iterator yielding all ["<current_word>", "<count>"] items
    for current_word, iter in groupby(data):
        try:
            # We select [0] to present the word in str format
            
            print ('%s' % (current_word[0]))
        except ValueError:
            pass

if __name__ == "__main__":
   main()
