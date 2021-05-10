# rending the twitter page
# from flask import Flask, request,jsonify
# from tweet_store import TweetStore

# store = TweetStore()
# tweets = store.tweets()


from flask import Flask, request,jsonify,Response
from tweet_store import TweetStore
import json

store = TweetStore()
tweets = store.tweets()


app = Flask(__name__)

@app.route('/tweet',methods=['GET', ])
def index():
  try:
    data =[tweet.data for tweet in tweets]
    return Response(response=json.dumps(data),mimetype="application/json")

  except Exception as e:
    return jsonify({"error":"server error"}),500
  





