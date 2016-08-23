import settings

#Collect tweets
results = settings.api.search(q='CBB', count=600)
tweets = []
for (idx, tweet) in enumerate(results[0:600]):
    tweets.append(results[idx].text)

#Define features
with open("positive-words.txt") as pos:
    pos_words = pos.readlines()
with open("negative-words.txt") as neg:
    neg_words = neg.readlines()