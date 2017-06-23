import tweepy
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_columns = 50
pd.options.display.max_rows= 50
pd.options.display.width= 120

consumer_key = 'aWvnzwNqFo0LdpxYTZD1CNB0f'
consumer_secret = 'Iwu6Txzgy6ZXkbCjJ7UiUglf99V4qY9Kd7xWIs96M6VXtcvZ2h'

access_token = '808076343292362752-fnUeydGjzzxbvliuX6LaWQTrJDvZzUl'
access_token_secret = 'RkCsaDYS3lLAyAYESzLZAoqlPWXQIClHZwhs1rRukb7Yn'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



def process_results(results):
    id_list = [tweet.id for tweet in results]
    data_set = pd.DataFrame(id_list, columns=["id"])

    # Processing Tweet Data

    data_set["text"] = [tweet.text for tweet in results]
    data_set["created_at"] = [tweet.created_at for tweet in results]
    data_set["retweet_count"] = [tweet.retweet_count for tweet in results]
    data_set["favorite_count"] = [tweet.favorite_count for tweet in results]
    data_set["source"] = [tweet.source for tweet in results]

    # Processing User Data
    data_set["user_id"] = [tweet.author.id for tweet in results]
    data_set["user_screen_name"] = [tweet.author.screen_name for tweet in results]
    data_set["user_name"] = [tweet.author.name for tweet in results]
    data_set["user_created_at"] = [tweet.author.created_at for tweet in results]
    data_set["user_description"] = [tweet.author.description for tweet in results]
    data_set["user_followers_count"] = [tweet.author.followers_count for tweet in results]
    data_set["user_friends_count"] = [tweet.author.friends_count for tweet in results]
    data_set["user_location"] = [tweet.author.location for tweet in results]

    return data_set


#API.search(q[, lang][, locale][, rpp][, page][, since_id][, geocode][, show_user])
tweets = []
for tweet in tweepy.Cursor(api.search, q="Mbappe Arsenal", lang="en").items(100):
    tweets.append(tweet)

print(len(tweets))
#
# for tweet in tweets:
#     analysis = TextBlob(tweet.text)
#     print(tweet.text)

data_set = process_results(tweets)

# data_set.to_csv('data_set.txt', sep='\t', encoding='utf-8')

sources = data_set["user_location"].value_counts()[:5][::-1]

plt.barh(range(len(sources)), sources.values)
plt.yticks(np.arange(len(sources)) + 0.4, sources.index)
plt.show()