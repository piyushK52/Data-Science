import sys
import json
import string

def nword(word):
    exclude = set(string.punctuation)
    word = ''.join(ch for ch in word.lower() if ch not in exclude)
    return word

def senti_val(senti_dict,line):
    score = 0
    for word in line.split(' '):
        if word in senti_dict:
            score += senti_dict[word]
    return score

def geo_info(tweet):
    if all(k in tweet.keys() for k in ("text","id","place")):
        if tweet['place'] is not None and "country_code" in tweet['place'].keys():
            if tweet['place']['country_code'] == 'US':
                state = tweet['place']['full_name'][-2:]
                return True,state
            else:
                return False,''
        return False,''


def main():
    
    senti_file = open(sys.argv[1])
    senti_dict = {} 
    for line in senti_file:
        term, score  = line.split("\t")  
        senti_dict[term] = int(score)  
    tweet_file = open(sys.argv[2])
    state_happy_index = {}
    total_tweet_count = 0

    for line in tweet_file:
        d = json.loads(line.encode('utf8'))
        if 'text' in d.keys(): 
            tweet = nword(d['text'].encode('utf8'))
            #print "type of flag",type(flag)
            #print "type of state",type(state)
            flag,state = geo_info(d)
            if flag:
                total_tweet_count += 1
                score = senti_val(senti_dict,tweet)
                if state in state_happy_index:
                    state_happy_index[state] += score
                else:
                    state_happy_index[state] = score
    
    happiest_state = 'NULL'
    happy_score = -1

    for state in state_happy_index.keys():
        if state_happy_index[state] > happy_score:
            happy_score = state_happy_index[state]
            happiest_state = state
            
    print happiest_state

if __name__ == '__main__':
    main()



