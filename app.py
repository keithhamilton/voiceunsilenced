#!/usr/bin/env python

from flask import Flask, request
import twilio.twiml

app = Flask(__name__)

@app.route("/fetch", methods=['GET', 'POST'])
def twiml_gen():
    tweet_from = request.args.get('from')
    from_msg = request.args.get('from_msg')
    tweet = request.args.get('tweet')

    resp = twilio.twiml.Response()
    resp.record()
    resp.say(from_msg)
    resp.pause()
    resp.say(tweet)
    resp.say('...')
    resp.say('We are unsilenced.')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
