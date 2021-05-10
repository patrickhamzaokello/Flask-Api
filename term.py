from tweet_store import TweetStore

store = TweetStore()
tweets = store.tweets()


for tweet in tweets:
	print(tweet)