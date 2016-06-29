# BBUKEvictionPredictor
A program that uses twitter sentiment analysis to predict the next contestant to be evicted on Big Brother UK.

Program Rundown
- The program collects recent past tweets tagged BBUK (Big Brother UK)
- It then uses lists of positive and negative words to model a sentiment analyzer
- The sentiment analyzer keeps a tally of the negative tweets directed at each individual housemate
- The housemate with the highest number of negative tweets is supposed to be the next houseguest to get evicted

Sentiment Analyzer Versions
- I first tried using the nltk sentiment analyzer to categorize the tweets however this led to a lot of false negatives
- I then used a rule-based sentiment analyzer, which draws upon precategorized lists of positive and negative words.  This turned out to be a lot more reliable.

To Dos
- Use statistical methods to determine the algorithm's accuracy and precision
- Update sentiment analyzer to accomodate for negation