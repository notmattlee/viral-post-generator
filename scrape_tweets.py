import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape_tweets(keyword="AI", limit=10):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(keyword).get_items()):
        if i >= limit:
            break
        tweets.append({
            "Tweet": tweet.content,
            "Username": tweet.user.username,
            "Date": tweet.date.strftime('%Y-%m-%d'),
        })
    return pd.DataFrame(tweets)
