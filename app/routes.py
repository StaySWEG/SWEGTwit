
from app import app
from flask import Flask, request
from flask import render_template
from .controllers.twitter_client import TwitterClient
from .controllers.file_writer import FileWriter
from .controllers.row import Row

@app.route('/results', methods=['POST'])
def result_set():
    """ Retrieve the form data """
    since_date  = request.form['sinceDate']
    to_date     = request.form['toDate']
    keywords    = request.form['keywords'].split(',') # Split since they're separated by coma
    num_tweets  = request.form['numTweets']

    """ Debug """
    print( "#########################################################" )
    print( "Looking for tweets that meet this filters:" )
    print( "Since date: " + since_date )
    print( "To date: "    + to_date )
    print( "With this keywords: ", end='')

    for keyword in keywords:
        print(keyword, end=' ')

    print( "\nNumber of tweets to be downloaded: " + num_tweets)    
    print( "#########################################################")

    """ Create Twitter client """
    client      = TwitterClient()

    """ Download tweets """
    keywords.append("-filter:retweets")
    tweets = client.getTweets(since_date, to_date, num_tweets, keywords)


    """ Create table of tweets """
    result_table = []
    for tweet in tweets:
        row = Row(tweet.user.screen_name, tweet.user.location, tweet.text.replace('\n', ' '))
        result_table.append(row)

    """ Write file .csv """
    file_writer = FileWriter()
    file_writer.write_tweets_csv("result_set.csv", result_table)

    return render_template('results.html', title="Results", result_table=result_table)


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
@app.route('/home',methods=['POST', 'GET'])
def index():
    """ Home screen """
    return render_template('index.html', title="Home")