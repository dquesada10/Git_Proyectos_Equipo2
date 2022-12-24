#!/usr/bin/env python3
"""A more advanced Mapper, using Python iterators and generators."""
 
import sys, json

def maper(record, separator):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        print ('%s%s%s' % (w, separator, key))

 
def main(inputdata, separator='\t'):
    # input comes from STDIN (standard input)
    for line in inputdata:
        record = json.loads(line)
        maper(record, separator)
 
if __name__ == "__main__":
    inputdata = open(sys.argv[1])
    main(inputdata)