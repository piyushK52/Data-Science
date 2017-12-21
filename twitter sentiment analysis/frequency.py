import sys
import json
import string

def update_dict(dct,tweet):
	for word in tweet.split():
		if word in dct:
			dct[word] += 1
		else:
			dct[word] = 1

def nword(word):
    exclude = set(string.punctuation)
    word = ''.join(ch for ch in word.lower() if ch not in exclude)
    return word

def main():
	dct = {}
	tweet_file = open(sys.argv[1])
	for line in tweet_file:
		d = json.loads(line.encode('utf8'))
		if 'text' in d.keys():
			update_dict(dct,nword(d['text'].encode('utf8')))

	all_occ = sum(dct.values())
	for word in dct.keys():
		print word,dct[word]/float(all_occ)


if __name__ == '__main__':
    main()