#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
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

current = datetime.datetime.now()
deadline = datetime.datetime(2017, 1, 17, 13, 0, 0, 0)
diff = deadline - current
days = diff.days
hours = diff.seconds / 3600 + days * 24

text = u'最終発表会まであと%d日(%d時間)です。' % (days, hours)

# ツイートを送信
try:
    api.update_status(status=text)
except tweepy.TweepError as e:
    print e
