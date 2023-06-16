import os
import logging

import tweepy
import requests
logger = logging.getLogger("twitter")

twitter_client = tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_SECRET"],
)


logger = logging.getLogger("twitter")

auth = tweepy.OAuthHandler(
    os.environ.get("TWITTER_API_KEY"), os.environ.get("TWITTER_API_SECRET")
)
auth.set_access_token(
    os.environ.get("TWITTER_ACCESS_TOKEN"), os.environ.get("TWITTER_ACCESS_SECRET")
)
api = tweepy.API(auth)


def scrape_user_tweets(username, num_tweets=5):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    """

    tweets = api.user_timeline(screen_name=username, count=num_tweets)
    response = requests.get(
        "https://gist.github.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/eden-marco.json"
    )
    data = response.json()
    # user_id = twitter_client.get_user(username=username).data.id
    # tweets = twitter_client.get_users_tweets(
    #     id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
    # )

    tweet_list = []
    for tweet in data.data:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
        tweet_list.append(tweet_dict)

    return tweet_list


# if __name__ == "__main__":
#     print(scrape_user_tweets(username="hwchase17"))
