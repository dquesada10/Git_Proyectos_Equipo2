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
    # groupby groups multiple word-doc_id pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["<current_word>", "<doc_id>"] items
    
    for current_word, group in groupby(data, itemgetter(0)):
        total_list=[]
        try:
            for current_word, doc_id in group:
                s=str(doc_id)
                if s not in total_list:
                    total_list.append(s)
            print ("%s%s%s" % (current_word, separator, str(total_list)))
        except ValueError:
            #doc_id was not valid
            pass

if __name__ == "__main__":
   main()
