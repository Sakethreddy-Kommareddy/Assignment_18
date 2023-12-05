from flask import Flask, request, jsonify
import json

app =Flask(__name__)

with open('100tweets.json', 'r', encoding='utf-8') as file:
    tweets = json.load(file)
    
@app.route('/')
def welcome():
    return 'Welcome to Saint Louis University celebrating the Winter Fest ❤️❤️❤️💕❤️❤️❤️🎈🎁'

@app.route('/tweets', methods=['GET'])
def get_all_tweets():
    try:
        return jsonify(tweets)
    except Exception as e:
        return str(e), 500
    
@app.route('/tweets_filtered', methods=['GET'])
def get_filtered_tweets():
    try:
        keyword = request.args.get('keyword')
        if keyword:
            filtered_tweets = [tweet for tweet in tweets if keyword.lower() in tweet['text'].lower()]
            return jsonify(filtered_tweets)
        return jsonify(tweets)
    except Exception as e:
        return str(e), 500