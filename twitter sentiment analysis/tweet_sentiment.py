import sys
import json
import string

def nword(word):
    exclude = set(string.punctuation)
    word = ''.join(ch for ch in word.lower() if ch not in exclude)
    return word

def senti_val(senti_dict,line):
	senti_score = 0
	for word in line.split(' '):
		if word in senti_dict:
			senti_score += senti_dict[word]
	return senti_score

def main():
   s_file = open(sys.argv[1])
   senti_dict={}
   for line in s_file:
       term, score = line.split("\t")
       senti_dict[term] = int(score)
   tweet_file = open(sys.argv[2])
   for line in tweet_file:
       #print (type(line))
       d = json.loads(line)
       if 'text' in d.keys():
           tweet = nword(d['text'])
           print (senti_val(senti_dict,tweet))

if __name__ == '__main__':
    main()