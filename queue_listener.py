#!/usr/bin/env python

import json
import os
import random
import urllib

import redis
import tweepy
from twilio.rest import TwilioRestClient


### GLOBALS ###

# REDIS
REDIS_LIST = 'tweets'
REDIS_CLIENT = redis.StrictRedis.from_url(os.environ['REDIS_URL'])

# TWITTER KEYS
CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

TWITTER_AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
TWITTER_AUTH.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
TWITTER_API = tweepy.API(TWITTER_AUTH)
TWITTER_BOT = os.environ['TWITTER_BOT_HANDLE']

# TWILIO NUMBERS/NAMES
if os.environ['ENV'] == 'PROD':
    names = os.environ['CONGRESS_NAMES']
    numbers = os.environ['CONGRESS_NUMBERS']
    NUMBER_POOL = dict(zip(numbers.split(','), names.split(',')))
else:
    name = os.environ['TEST_NAME']
    number = os.environ['TEST_NUMBER']
    NUMBER_POOL = {number: name}

twilio_numbers = os.environ['TWILIO_PHONE_NUMBERS'].split(',')
victims = os.environ['TWILIO_FROM_NAMES'].split(',')
if len(victims) != len(twilio_numbers):
    victims = victims * len(twilio_numbers)

VICTIM_NUMBERS = dict(zip(twilio_numbers, victims))


class StreamListener(tweepy.StreamListener):

    """
    Class derived from Tweepy StreamListener that implements custom behavior
    for the on_status handler function.
    """

    def on_status(self, status):

        """
        Defines logic to perform when a tweet is received. Ensures tweet
        did not originate from the Twitter bot we are using, cleans and
        wraps up the relevant tweet information, then queues it in Redis.

        Args:
            status (dict): Tweepy status object containing all information
                           for a given tweet.

        Returns:
            None
        """

        if status.user.screen_name == TWITTER_BOT:
            return

        print(status.text)
        print(status.user.screen_name)

        _status = status.text.replace('@{} '.format(TWITTER_BOT), '')
        clean_tweet = _status.encode('utf-8').strip()

        tweet = {
            'text': clean_tweet,
            'sender': status.user.screen_name,
            'sender_name': status.user.name,
            'tweet_id': status.id,
            }

        enqueue(tweet)

def enqueue(tweet):

    """
    Performs the queueing of a tweet into the Redis list that the queue
    worker consumes.

    Args:
        tweet (dict): dict object containing all of the critical elements
                      for a given Tweet.
    Returns:
        None
    """

    _to = random.choice(NUMBER_POOL.items())
    _from = random.choice(VICTIM_NUMBERS.items())

    tweet_string = json.dumps({'to': _to, 'from': _from, 'tweet': tweet})

    REDIS_CLIENT.rpush(REDIS_LIST, tweet_string)


def listen():

    """
    Listens to the Twitter bot's stream for activity, using the custom
    StreamListener created above.

    Returns:
        None
    """

    print('listening to {}'.format(TWITTER_BOT))

    try:
        listener = StreamListener()
        stream = tweepy.Stream(auth = TWITTER_API.auth, listener=listener)
        stream.filter(track=[TWITTER_BOT])

    except Exception as e:
        print(e)
        listen()


if __name__ == '__main__':

    listen()
