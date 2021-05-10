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

@app.route("/")
def index():
    return "<div style='display:grid; place-content:center'><div style='background: #f7f7f7;padding: 1em 2em;color: black;margin: 0 auto;width: 300px;'>You Landed Well, Click <a href='tweet'>kasfa api</a></div></div>"
    # return "welcome"


@app.route('/tweet',methods=['GET', ])
def tweet():
  try:
    data =[tweet.data for tweet in tweets]
    return Response(response=json.dumps(data),mimetype="application/json")

  except Exception as e:
    return jsonify({"error":"server error"}),500
  





