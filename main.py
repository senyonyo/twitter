#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import secret
import codecs

CK= secret.twkey['ck']
CS= secret.twkey['cs']
ATK= secret.twkey['atk']
ATS= secret.twkey['ats']

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(ATK, ATS)
api = tweepy.API(auth_handler=auth)

#api.update_status("Hello, world!")
keyword = "lang:ja min_retweets:50"

def search_rest(api,keyword,search_count=10):
  search_result = api.search(keyword,count=search_count)
  for i,twt in enumerate(search_result):
    print"---%3d---" % (i + 1)
    print twt.created_at
    print twt.user.name
    print twt.text +"\n"
    
    with open('tweet.txt','a') as f:
      f.write("%3" % (i+1))
      f.write(str(twt.created_at).encode('utf-8'))
      f.write(twt.user.name.encode('utf-8'))
      f.write((twt.text+"\n").encode('utf-8'))

search_rest(api,keyword,30)
