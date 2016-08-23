#Classification algorithm
def sentimenter(words_in_tweet):
    tweet_pos_words = 0
    tweet_neg_words = 0
    tweet_neu_words = 0
    sent_score = ""
    
    for word in words_in_tweet:
        
        if word+'\n' in pos_words:
            tweet_pos_words += 1
        elif word+'\n' in neg_words:
            tweet_neg_words += 1
        else:
            tweet_neu_words += 1
    #print('pos: ', tweet_pos_words, '| neg: ', tweet_neg_words, '| neu: ', tweet_neu_words)
    
    if tweet_pos_words > tweet_neg_words:
        sent_score += 'pos'
    elif tweet_neg_words > tweet_pos_words:
        sent_score += 'neg'
        housemates[name] += 1
    else:
        sent_score += 'neu'
    #print(sent_score)