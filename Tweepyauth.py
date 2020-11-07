import tweepy
consumer_key="LrQcFkiHT7KlkVGptMwV0LRN3"
consumer_secret="wrWpA4ZEWbbN2YujSRCmECfoCU3ny7F5krTpFYXafIR5cEyWL3"
access_token="968018325484613632-AqfjeSYCXR4ctyTmPQI6O0E6QS2Qrmj"
access_token_secret="OSsbILA8dr86w5mj4MatIPKhZREgkXbwWcghFpZQYYbDs"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)