#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import secret
import codecs
import MySQLdb
import time
import datetime
import 
connector = MySQLdb.connect(host='localhost',port=3306,user="root",passwd='Densuke3!',db='tweets_collection',charset='utf8')
cursor = connector.cursor()

CK= secret.twkey['ck']
CS= secret.twkey['cs']
ATK= secret.twkey['atk']
ATS= secret.twkey['ats']

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(ATK, ATS)
api = tweepy.API(auth_handler=auth)

keyword = "lang:ja min_retweets:50"

def search_rest(api,keyword,search_count=10):
  search_result = api.search(keyword,count=search_count)
  for i,twt in enumerate(search_result):
#   print (int(time.mktime(twt.created_at.timetuple())),twt.user.name.encode('utf8'),int(twt.user.id),twt.text.encode('utf8'),int(twt.id),int(twt.retweet_count),int(twt.favorite_count))
#   cursor.execute(
#     'insert into tweets'
#     '(date,username,userid,text,textid,rt,fav)'
#     'VALUES (%s,%s,%s,%s,%s,%s,%s)',
#     (int(time.mktime(twt.created_at.timetuple())),twt.user.name.encode('utf8'),int(twt.user.id),twt.text.encode('utf8'),int(twt.id),int(twt.retweet_count),int(twt.favorite_count))
#   )
#   connector.commit()

#   cursor.close()
# 
# connector.close()
 
   with open('tweet.txt','a') as f:
     f.write(str(i+1))
     f.write(str(int(time.mktime(twt.created_at.timetuple()))).encode('utf-8')+"\n")
     f.write(twt.user.name.encode('utf-8')+"\n")
     f.write(twt.text.encode('utf-8')+"\n")
     f.write(str(int(twt.retweet_count)).encode('utf-8')+"\n")
     f.write(str(int(twt.favorite_count)).encode('utf-8')+"\n")
     f.write("\n")

search_rest(api,keyword,30)

