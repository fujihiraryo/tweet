from requests_oauthlib import OAuth1Session
import json
import requests
import secret

session = OAuth1Session(secret.API_KEY, secret.API_SECRET_KEY,
                        secret.ACCESS_TOKEN, secret.ACCESS_TOKEN_SECRET)
timeline_url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
tweet_url = "https://api.twitter.com/1.1/statuses/update.json"

if session.get(timeline_url).status_code != 200:
    print("しばらく待ってから試してくれ")
    exit()

while True:
    timeline = session.get(timeline_url).json()[:10]
    timeline.reverse()
    for tweet in timeline:
        print(tweet["id"])
        print(tweet["created_at"])
        print(tweet["user"]["name"]+" @"+tweet["user"]["screen_name"])
        print(tweet["text"])
        print("retweet:"+str(tweet["retweet_count"]) +
              " favorite:"+str(tweet["favorite_count"]))
        print("-----------------------------")
    text = input("tweet >> ")
    if text == "exit":
        exit()
    elif text != "":
        session.post(tweet_url, params={'status': text})
