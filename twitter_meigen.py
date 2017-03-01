#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import choice
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

meigen = []
for line in open('meigen.txt','r'):
    line = line.rstrip()
    meigen.append(line)

# choice はリストから一つランダムに選択
text = choice(meigen)

# ツイートを送信
try:
    api.update_status(status=text)
except tweepy.TweepError as e:
    print e
