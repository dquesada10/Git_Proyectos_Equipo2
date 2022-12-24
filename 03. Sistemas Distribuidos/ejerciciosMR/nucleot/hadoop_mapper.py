#!/usr/bin/env python3
"""A more advanced Mapper, using Python iterators and generators."""
 
import sys, json

def maper(record, separator):
    # key: it comes from value and then we cut the first 10 chars
    value = record[1]
    print ('%s' % (value[:10]))

 
def main(inputdata, separator='\t'):
    # input comes from JSON file
    for line in inputdata:
        record = json.loads(line)
        maper(record, separator)
 
if __name__ == "__main__":
    inputdata = open(sys.argv[1])
    main(inputdata)