#!/usr/bin/env python3
"""A more advanced Reducer, using Python iterators and generators."""
 
from itertools import groupby
from operator import itemgetter
import sys, json
 
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
    jenc = json.JSONEncoder()
    for key, group in groupby(data, itemgetter(0)):
        cum_sum, prev_pos, product = [0, -1, 1]
        try:
            for key, value in group:
                # print ("key es%s"%key)
                # print ("value es%s"%value)
                pos=int(value.split("\t")[0])
                # print ("pos es%s"%pos)
                if pos == prev_pos:
                    product=product*int(value.split("\t")[1])
                    # print("product es%d"%product)
                    cum_sum=cum_sum+product
                    # print("cum_sum es  %d"%cum_sum)
                else:
                    product= int(value.split("\t")[1])
                    prev_pos= pos
            result=["c", int(key.split("_")[0]), int(key.split("_")[1]), cum_sum]
            print (jenc.encode(result))
            # print ("%s%s%s%s%s%s%d" % ("c", separator, key.split("_")[0], separator, key.split("_")[1], separator, cum_sum))
        except ValueError:
            #count was not a number
            pass

if __name__ == "__main__":
   main()
