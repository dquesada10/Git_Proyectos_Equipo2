#!/usr/bin/env python3
"""A more advanced Mapper, using Python iterators and generators."""
 
import sys, json

def maper(record, separator):
    # key: document identifier
    # value: document contents
    numcol = 5
    matriz, fila, columna, value = record
    pos= (columna if matriz=="a" else fila)

    for i in range(numcol):
        key=(str(fila)+"_"+str(i) if matriz == "a" else str(i)+"_"+str(columna))
        print ('%s%s%s%s%d' % (key, separator, pos, separator, value))
 
def main(inputdata, separator='\t'):
    # input comes from STDIN (standard input)
    for line in inputdata:
        record = json.loads(line)
        maper(record, separator)
 
if __name__ == "__main__":
    inputdata = open(sys.argv[1])
    main(inputdata)