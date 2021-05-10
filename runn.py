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


def application()->Flask:
  app = Flask(__name__)

  @app.route('/tweet',methods=['GET', ])
  def twitthandler():
    try:
      data =[tweet.data for tweet in tweets]

      print(json.dumps(data))

      return Response(response=json.dumps(data),mimetype="application/json")

    except Exception as e:
      return jsonify({"error":"server error"}),500
  
     
  return app

if __name__ == "__main__":

  application().run("0.0.0.0", port=5003, debug=True)



