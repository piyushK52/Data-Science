import MapReduce
import json 
import sys

def mapper(record):
    dim = 5
    if record[0] == 'a':
        for i in range(dim):
            mr.emit_intermediate(str(record[1])+' '+str(i), record)

    elif record[0] == 'b':
        for i in range(dim):
            mr.emit_intermediate(str(i)+' '+str(record[2]),record)


def reducer(key, list_of_values):
    res = 0
    add = key.split(' ')
    #print "here for "+add[0]+" "+add[1]
    for l1 in list_of_values:
        for l2 in list_of_values:
            if l1[0]!=l2[0] and l1[0]=='a' and l1[2]==l2[1]:
                res += l1[-1]*l2[-1]
    mr.emit((int(add[0]),int(add[1]),res))


mr = MapReduce.MapReduce()
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
