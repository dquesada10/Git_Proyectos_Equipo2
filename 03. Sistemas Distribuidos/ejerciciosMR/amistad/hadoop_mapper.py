#!/usr/bin/env python3
"""A more advanced Mapper, using Python iterators and generators."""
 
import sys, json

def maper(record, separator):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    print ('%s%s%s%s%d' % (key, "_", value, separator, 0))
    print ('%s%s%s%s%d' % (value, "_", key, separator, 1))
    
def main(inputdata, separator='\t'):
    # input comes from STDIN (standard input)
    for line in inputdata:
        record = json.loads(line)
        maper(record, separator)
 
if __name__ == "__main__":
    inputdata = open(sys.argv[1])
    main(inputdata)