#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy

consumer_key        = ''
consumer_secret     = ''
access_token        = ''
access_token_secret = ''

# Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# Twitter API
api = tweepy.API(auth)

followers = api.followers()
for user in followers:
    screen_name = user.screen_name
    print screen_name
    tweets = api.user_timeline(screen_name=screen_name, count=5)
    for tweet in tweets:
        print tweet.id, tweet.text
