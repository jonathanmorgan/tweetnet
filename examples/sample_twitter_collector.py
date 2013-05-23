# imports
import datetime
import twitter
import tweetnet.models
from python_utilities.django_utils.django_string_helper import DjangoStringHelper

# set up OAuth stuff.
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# Make an OAuth object.
my_oauth = twitter.OAuth( ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET )

#================================================================================
# Tweet Stream collection
#================================================================================

# Create a tweetstream
twitter_stream = twitter.TwitterStream( auth = my_oauth )

# get an iterator over tweets
tweet_iterator = twitter_stream.statuses.sample()

# loop over tweets
tweet_counter = 0
for current_tweet in tweet_iterator:

    # check for delete request.
    try:
    
        # if delete request, will have a delete element at the root.
        # If not, this will throw an exception, and you'll process the tweet.
        delete_info = current_tweet[ 'delete' ]
        print( "--> Deletion request - moving on." )
    
    except:

        # create a tweet object.
        tweet_db = tweetnet.models.Tweet()
        tweet_db.twitter_tweet_id = current_tweet[ 'id' ]
        tweet_db.tweet_text = DjangoStringHelper.encode_string( current_tweet[ 'text' ], entitize_4_byte_unicode_IN = True )
        tweet_db.tweet_timestamp = current_tweet[ 'created_at' ]
        tweet_db.tweet_timestamp_dt = datetime.datetime.strptime( tweet_db.tweet_timestamp, tweetnet.models.TWITTER_DATE_FORMAT )
        tweet_db.timestamp_year = tweet_db.tweet_timestamp_dt.year
        tweet_db.timestamp_month = tweet_db.tweet_timestamp_dt.month
        tweet_db.timestamp_day = tweet_db.tweet_timestamp_dt.day
        tweet_db.timestamp_hour = tweet_db.tweet_timestamp_dt.hour
        tweet_db.timestamp_minute = tweet_db.tweet_timestamp_dt.minute
        tweet_db.timestamp_second = tweet_db.tweet_timestamp_dt.second
        tweet_db.twitter_user_twitter_id = current_tweet[ 'user' ][ 'id' ]
        tweet_db.twitter_user_screenname = current_tweet[ 'user' ][ 'screen_name' ]
        tweet_db.user_follower_count = current_tweet[ 'user' ][ 'followers_count' ]
        tweet_db.user_favorites_count = current_tweet[ 'user' ][ 'favourites_count' ]
        tweet_db.user_created = current_tweet[ 'user' ][ 'created_at' ]

        # save to database
        tweet_db.save()

    #-- END 
    
#-- END loop over tweet stream --#