# set up OAuth stuff.
CONSUMER_KEY = '<your_application_consumer_key>'
CONSUMER_SECRET = '<your_application_consumer_secret>'
ACCESS_KEY = '<your_user_application_access_key>'
ACCESS_SECRET = '<your_user_application_access_secret>'

#===============================================================================
# Trying twitter library used in O'Reilly books (not working great so far).
# from: https://github.com/sixohsix/twitter
# pip install twitter/pip uninstall twitter
#
# I think you have to install straight from git for this to work:
# pip install -e git+http://github.com/sixohsix/twitter.git#egg=github-pip-install
#
# Just using python-OAuth2 is easy enough, though, that I don't think I need one of these libraries.
#===============================================================================
# Python code for interacting with twitter using twitter library.

import twitter

# connect with OAuth.
t = twitter.Twitter(
    auth = twitter.OAuth( ACCESS_KEY, ACCESS_SECRET,
               CONSUMER_KEY, CONSUMER_SECRET ) )

# pull public statuses.
t.statuses.public_timeline()
               
# get a particular friend's timeline
t.statuses.friends_timeline( id = "hyfq" )

# try search:
twitter_search = twitter.Twitter(domain="search.twitter.com")

# try to get a twitter stream
twitter_stream = twitter.TwitterStream( twitter.OAuth( ACCESS_KEY, ACCESS_SECRET,
               CONSUMER_KEY, CONSUMER_SECRET ) )

#===============================================================================
# python-twitter library (imported as "twitter" also, have one or the other installed).
# From http://code.google.com/p/python-twitter/
# pip install python-twitter/pip uninstall python-twitter
#===============================================================================

import twitter

api = twitter.Api()

# authenticated via OAuth:
api = twitter.Api( consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET, access_token_key = ACCESS_KEY, access_token_secret = ACCESS_SECRET )

# latest public statuses
statuses = api.GetPublicTimeline()
print [s.user.name for s in statuses]

# user's latest public statuses, where "user" is either a Twitter "short name" or their user id.
statuses = api.GetUserTimeline( 'hyfq' )
print [s.text for s in statuses]

# the above only works on unprotected users, or protected users who have accepted a follow request.
# try an unprotected user...
statuses = api.GetUserTimeline( 'twitter' )
print [s.text for s in statuses]

# To fetch a list a user's friends (requires authentication):
users = api.GetFriends()
print [u.name for u in users]

#===============================================================================
# Another option - tweepy - need this to support streaming API.
#===============================================================================

import tweepy

# authenticate
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# print name.
print api.me().name

# so, it works.  Now need to either figure out how to use it to pull in other users' tweets, or just need to bite the bullet and learn and use oauth directly.

#===============================================================================
# Yet another option - twython (no streaming support).
# From https://github.com/ryanmcgrath/twython
# pip install twython/pip uninstall twython
#===============================================================================

#===============================================================================
# Built django models to hold tweets and twitter users.  Try interacting with
#    them to find users we will query.  Most easily run using the django shell:
#    in your django site's root directory (where the file manage.py is located),
#    run: python manage.py shell
#===============================================================================

# import tweetnet
import research.tweetnet

# specifically import Twitter_User
from research.tweetnet.models import Twitter_User

# get all users with more than 10 tweets (limit 10).
user_qs = Twitter_User.objects.filter( tweet_count__gt = 10 )

# get a count
user_qs.count() # 13,753

# order by tweet_count desc
user_qs = user_qs.order_by( '-tweet_count' ) 

# grab the first ten.
user_qs = user_qs[ 0 : 10 ]

# set up python-twitter
import twitter

api = twitter.Api()

# authenticated via OAuth:
api = twitter.Api( consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET, access_token_key = ACCESS_KEY, access_token_secret = ACCESS_SECRET )

# try just one user.
twitter_user = user_qs[0]
statuses = api.GetUserTimeline( twitter_user.twitter_user_name )
# strange errors.

# loop over users, grabbing and outputting the public timeline of each.
for twitter_user in user_qs:
    
    # grab and print the public timeline for the user.
    print( "===== " + twitter_user.twitter_user_name + " =====\n" )
    statuses = api.GetUserTimeline( twitter_user.twitter_user_name )
    print [s.text for s in statuses]
    print( "===== END " + twitter_user.twitter_user_name + " =====\n\n" )

#-- END loop over users - which didn't work --#

# There are since_id and max_id thingers, so you can only get new (since_id) or
#    step back through the user's public timeline (max_id, set to earliest tweet
#    ID you have.

# Fine.  Trying this with straight OAuth2 library.
import oauth2 as oauth

# initialize consumer (application-level secret).
consumer = oauth.Consumer( key = CONSUMER_KEY, secret = CONSUMER_SECRET )

# create user's application token
token = oauth.Token( key = ACCESS_KEY, secret = ACCESS_SECRET )

# make client
client = oauth.Client( consumer, token )

# retrieve timeline for user
resp, content = client.request( 'https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=' + twitter_user.twitter_user_name + '&count=2', 'GET' )

# Error in API doc.  Trying something really basic.
resp, content = client.request( 'https://api.twitter.com/1/trends/1.json', 'GET' )

# works.  So, what up with user_timeline? Try example URL on their page.
resp, content = client.request( 'https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=twitterapi&count=2', 'GET' )

# works.  404 error can mean that the user doesn't exist.  User with most tweets
#    in sample ("REMAXSINGH") appears to no longer exist.  Try next ("JwForum").
twitter_user = user_qs[1]
resp, content = client.request( 'https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=' + twitter_user.twitter_user_name + '&count=2', 'GET' )

# That one works, too.  So, 404 when you have the URL correct means user not
#    found.