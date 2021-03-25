from requests_oauthlib import OAuth1Session
import sys
import os


def tweet():
    session = OAuth1Session(
        os.environ["TWITTER_API_KEY"],
        os.environ["TWITTER_API_SECRET_KEY"],
        os.environ["TWITTER_ACCESS_TOKEN"],
        os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
    )
    tweet_url = "https://api.twitter.com/1.1/statuses/update.json"
    text = " ".join(sys.argv[1:])
    if text == "":
        print("Usage: tweet <text>")
        return
    session.post(tweet_url, params={"status": text})
    print(f"Successfully posted: {text}")
