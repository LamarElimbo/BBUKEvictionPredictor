import tweepy
import twitter_creds

AUTH = tweepy.OAuthHandler(twitter_creds.APP_KEY, twitter_creds.APP_SECRET)

AUTH.set_access_token(twitter_creds.ACCESS_TOKEN, twitter_creds.ACCESS_SECRET)

API = tweepy.API(AUTH)

CONTESTANTS = {'aubrey': 0, 'bear': 0, 'biggins': 0, 'chloe': 0, 'frankie': 0, 'grant': 0, 'heavy': 0, 'james': 0, 'katie': 0, 'lewis': 0, 'marnie': 0, 'renee': 0, 'ricky': 0, 'saira': 0, 'samantha': 0}