
import sys
import tweepy as tw
import pandas as pd
from .constants.keys import Keys

class TwitterClient:
    """ This class provides methods to interact with Twitter API """
    keys = None
    api = None

    def getTweets(self, since_date, to_date, num_tweets, *search_words):
        tweets = tw.Cursor(
            self.api.search,
            q=search_words,
            lang="it",
            since=since_date
        ).items(int(num_tweets))

        return tweets


    def __init__(self):
        self.keys = Keys()

        auth = tw.OAuthHandler(self.keys.consumer_key, self.keys.consumer_secret)
        auth.set_access_token(self.keys.access_token, self.keys.access_token_secret)
        self.api = tw.API(auth, wait_on_rate_limit = True)

