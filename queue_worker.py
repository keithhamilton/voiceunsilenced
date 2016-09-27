#!/usr/bin/env python

import json
import os
import redis
import time
import urllib

import tweepy
from twilio.rest import TwilioRestClient


APP_NAME = os.environ['BOT_APP_NAME']
WAIT_TIME = float(os.environ['WAIT_TIME'])

# REDIS
REDIS_LIST = 'tweets'
REDIS_CLIENT = redis.StrictRedis.from_url(os.environ['REDIS_URL'])

# TWILIO KEYS
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_CLIENT = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# TWITTER KEYS
CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

TWITTER_AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
TWITTER_AUTH.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
TWITTER_API = tweepy.API(TWITTER_AUTH)
TWITTER_BOT = os.environ['TWITTER_BOT_HANDLE']


def call(tweet):

    """
    Creates an outbound Twilio call to the Congressperson specified in the
    tweet object passed to it. Uses the to/from information in the `tweet`
    dict object to determine outboundnn phone number, number to be called,
    and message to be read.

    Args:
        tweet (dict): dict object containing all of the critical elements
                      for a given Tweet.

    Returns:
        None
    """

    (to_number, to_name) = tweet['to']
    (from_number, from_name) = tweet['from']
    _tweet = tweet['tweet']

    from_msg_str = 'This is a message from {} sent on behalf of {}'

    query = {
        'from_msg': from_msg_str.format(_tweet['sender_name'], from_name),
        'tweet': _tweet['text'],
        'tweet_from': _tweet['sender']
    }


    base_url = 'https://{}.herokuapp.com/fetch?{}'

    endpoint = base_url.format(APP_NAME, urllib.urlencode(query))
    call = TWILIO_CLIENT.calls.create(to=to_number, from_=from_number, url=endpoint)


def reply(tweet):

    """
    Replies to the incoming tweet that was transformed into a phone call to
    a Congressperson. If the tweet campe from the Twitter bot or the Twitter
    bot was @-mentioned in the tweet, return, so as to not create a loop.

    Args:
        tweet (dict): dict object containing all of the critical elements
                      for a given Tweet.

    Returns:
        None
    """

    tweeter = tweet['tweet']['sender']

    if tweeter == TWITTER_BOT or TWITTER_BOT in tweet['tweet']:
        return

    _tweet = tweet['tweet']
    tweet_id = _tweet['tweet_id']
    from_person = tweet['from'][1]
    to_person = tweet['to'][1]

    print(tweet['to'])
    msg_str = '@{}: {} was just called on behalf of {} #weareunsilenced'
    message = msg_str.format(tweeter, to_person, from_person)
    TWITTER_API.update_status(message, tweet_id)


def work():

    """
    Performs the main work on twests contained in Redis, waiting the amount
    of time specified by the environment var 'WAIT_TIME' in between calls.

    Returns:
        None
    """

    _, raw_tweet = REDIS_CLIENT.blpop(REDIS_LIST)
    tweet = json.loads(raw_tweet)

    call(tweet)
    reply(tweet)
    time.sleep(WAIT_TIME)


if __name__ == '__main__':

    while True:
        work()
