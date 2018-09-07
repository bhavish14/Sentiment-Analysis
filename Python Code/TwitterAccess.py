import tweepy

CONSUMER_KEY = 'AkKREMEgzDnXvCJ1n5bzWuMNK'
CONSUMER_SECRET = 'PS3IaMtUGDN7KLXTvSynhxakQ2qd2f6jsveLNt8YMEFzHGnnn2'
ACCESS_TOKEN = '3183846762-eOeKTJf2FTpqFlJ1DWNbJJ8QYwRhZcIKdjHDYPo'
ACCESS_TOKEN_SECRET = 'PYpl1gzDFNU9WU2l2FeFMRuPGOiWSd4TVqxoyhJeRZUKJ'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status = "Testing!"
api.update_status(status=status)
