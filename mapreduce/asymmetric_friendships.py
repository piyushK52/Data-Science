import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate(record[0], record[1]) 

def reducer(key, list_of_friends):
    for friend in list_of_friends:  
        try: 
            friends_list = mr.intermediate[friend]
            if (key not in friends_list):
                mr.emit((key, friend))
                mr.emit((friend, key))
        except KeyError:
                mr.emit((key, friend))
                mr.emit((friend, key))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)