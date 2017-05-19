# -*- coding: utf-8 -*-

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import secret

CK= secret.twkey['ck']
CS= secret.twkey['cs']
ATK= secret.twkey['atk']
ATS= secret.twkey['ats']

class StdOutListener(StreamListener):
    def on_data(self, data):
        if data.startswith("{"):
            print data
        return True
 
    def on_error(self, status):
        print status
 
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(CK,CS)
    auth.set_access_token(ATK, ATS)
 
    stream = Stream(auth, l)
    stream.filter(languages=['ja'], track=["a"])
    #    stream.sample()#ツイートのランダムサンプリングを取得する場合
#    stream.userstream()#タイムラインを取得する場合
