#Tokenize tweets and get sentiment score for tweet
from nltk import word_tokenize
import nltk
import sentimentClassifier

neg_tweets = []
type(tweets[0])

for tweet in tweets:
    tokenized_tweet = word_tokenize(tweet)
    tweet_words = [word.lower() for word in tokenized_tweet if word.isalpha() and len(word) > 2]
    for name in settings.CONTESTANTS.keys():
        if name in tweet_words:
            #print(name)
            #print(tweet)
            sentimentClassifier.sentimenter(tweet_words)

import matplotlib.pyplot as plt

plt.bar(range(len(settings.CONTESTANTS)), settings.CONTESTANTS.values(), align='center')
plt.xticks(range(len(settings.CONTESTANTS)), settings.CONTESTANTS.keys())

plt.show()