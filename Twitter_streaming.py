# Import the necessary methods from tweepy library
import status as status
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import matplotlib.pyplot as plt
import status
from datetime import datetime

# Variables that contains the user credentials to access Twitter API
access_token = "363692281-UESNA3QF48lIpmEasMNf7HqmJMes2X4o5ZIcwl3K"
access_token_secret = "4BGO9QsiXgVGjBCQDx3r8WquQVLzZ5gisHxITiqV1VdXI"
consumer_key = "XtUT6tf4SO5pIkIbMNEeudzzp"
consumer_secret = "DeqQFnoLq7x6XrE8d63xWtgbMHN97kQPhhPJQ3Zm2p9VfAKxhH"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['@RealDonalTrump', 'Trump', 'Administration', 'Cabinet'])

# Next we will read the data in into an array that we call tweets

tweets_data_path = '../Trump_data0122.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print(len(tweets_data))
