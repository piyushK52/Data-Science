import sys
import json
import string
import operator

def nword(word):
    exclude = set(string.punctuation)
    word = ''.join(ch for ch in word.lower() if ch not in exclude)
    return word

def main():
    s_file = open(sys.argv[1])
    h_dict={}
    for line in s_file:
        d = json.loads(line.encode('utf8'))
        if "entities" in d.keys():
            hashtags = d['entities']['hashtags']
            h_tags = []
            for tags in hashtags:
                t = nword(tags['text'].encode('utf8'))
                if t in h_dict:
                    h_dict[t]+=1
                else:
                    h_dict[t] = 1
    
    h_dict = sorted(h_dict.items(),key=operator.itemgetter(1),reverse=True)
    for i in range(10):
        print h_dict[i][0],h_dict[i][1]   

if __name__ == '__main__':
    main()
            
            
