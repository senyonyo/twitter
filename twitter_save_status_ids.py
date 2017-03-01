#!/usr/bin/python
# -*- coding: utf-8 -*-
from os.path import isfile
import fcntl
from fcntl import flock
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

# これまでに対応したstatus idのリスト格納用
data = []

if isfile('log.txt'):
    f = open('log.txt', 'r')
    flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    for line in f.readlines():
        data.append(int(line.strip()))
    flock(f, fcntl.LOCK_UN)
    f.close()
else:
    print 'Warning: log.txt not found'

# 自分への未応答のメンションのそれぞれについて応答
mentions = api.mentions_timeline(count=10)
for tweet in mentions:
    if not tweet.id in data:
        try:
            api.update_status(
                status='@%s Hello!' % (tweet.user.screen_name),
                in_reply_to_status_id=tweet.id
            )
            data.append(tweet.id)
        except tweepy.TweepError as e:
            print e
    else:
        print 'INFO: already replied %d' % tweet.id

# 更新された status_id のリストを書き出し
f = open('log.txt', 'w')
flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
for item in data:
    f.write('%d\n' % item)
flock(f, fcntl.LOCK_UN)
f.close()
