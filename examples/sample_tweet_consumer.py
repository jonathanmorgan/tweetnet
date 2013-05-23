# imports

# python base
import datetime
import time

# twitter modules
import twitter
import tweetnet.models

# python_utilities
from python_utilities.django_utils.django_string_helper import DjangoStringHelper

# set up OAuth stuff.
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# Make an OAuth object.
my_oauth = twitter.OAuth( ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET )

#================================================================================
# Tweet consumption
#================================================================================

# Create a Twitter instance
twitter_api = twitter.Twitter( auth = my_oauth )

# get ten tweets that don't yet have users.
tweet_sample = tweetnet.models.Tweet.objects.filter( twitter_user__isnull = True )[ : 10 ]

# loop over the user-less tweets.
tweet_counter = 0
for current_tweet in tweet_sample:

    # increment counter
    tweet_counter += 1
    
    # break out twitter ID.
    tweet_user_id = current_tweet.twitter_user_twitter_id

    # get user's information - eventually, check length of list.
    user_info_list = twitter_api.users.lookup( user_id = tweet_user_id, _timeout = 1 )
    user_info = user_info_list[ 0 ]
    
    # make and store a user instance.
    current_user_db = tweetnet.models.Twitter_User()
    
    # store data...
    current_user_db.twitter_user_name = user_info[ 'screen_name' ]
    current_user_db.twitter_user_twitter_id = user_info[ 'id' ]
    current_user_db.created_at = user_info[ 'created_at' ]
    current_user_db.created_at_dt = datetime.datetime.strptime( current_user_db.created_at, tweetnet.models.TWITTER_DATE_FORMAT )
    current_user_db.description = user_info[ 'description' ]
    current_user_db.followers_count = user_info[ 'followers_count' ]
    current_user_db.favourites_count = user_info[ 'favourites_count' ]
    current_user_db.location = user_info[ 'location' ]
    current_user_db.name = user_info[ 'name' ]
    current_user_db.lang = user_info[ 'lang' ]
    current_user_db.image_url = user_info[ 'profile_image_url' ]
    current_user_db.image_url_https = user_info[ 'profile_image_url_https' ]
    current_user_db.is_protected = user_info[ 'protected' ]
    current_user_db.is_geo_enabled = user_info[ 'geo_enabled' ]
    current_user_db.is_verified = user_info[ 'verified' ]
    current_user_db.time_zone = user_info[ 'time_zone' ]
    current_user_db.url = user_info[ 'url' ]
    current_user_db.utc_offset = user_info[ 'utc_offset' ]

    # save
    current_user_db.save()
    
    print( "==> " + str( tweet_counter ) + " - " + str( current_user_db ) )
    
    # add user to tweet and save
    current_tweet.twitter_user = current_user_db
    current_tweet.save()

    # get user's tweets
    current_user_tweet_list = twitter_api.statuses.user_timeline( user_id = tweet_user_id )
    
    # loop over user's tweets
    for current_user_tweet in current_user_tweet_list:
    
        # check for delete request.
        try:
        
            # if delete request, will have a delete element at the root.
            # If not, this will throw an exception, and you'll process the tweet.
            delete_info = current_user_tweet[ 'delete' ]
            print( "--> Deletion request - moving on." )
        
        except:
    
            # create a tweet object.
            tweet_db = tweetnet.models.Tweet()
            tweet_db.twitter_user = current_user_db
            tweet_db.twitter_tweet_id = current_user_tweet[ 'id' ]
            tweet_db.tweet_text = DjangoStringHelper.encode_string( current_user_tweet[ 'text' ], entitize_4_byte_unicode_IN = True )
            tweet_db.tweet_timestamp = current_user_tweet[ 'created_at' ]
            tweet_db.tweet_timestamp_dt = datetime.datetime.strptime( tweet_db.tweet_timestamp, tweetnet.models.TWITTER_DATE_FORMAT )
            tweet_db.timestamp_year = tweet_db.tweet_timestamp_dt.year
            tweet_db.timestamp_month = tweet_db.tweet_timestamp_dt.month
            tweet_db.timestamp_day = tweet_db.tweet_timestamp_dt.day
            tweet_db.timestamp_hour = tweet_db.tweet_timestamp_dt.hour
            tweet_db.timestamp_minute = tweet_db.tweet_timestamp_dt.minute
            tweet_db.timestamp_second = tweet_db.tweet_timestamp_dt.second
            tweet_db.twitter_user_twitter_id = current_user_tweet[ 'user' ][ 'id' ]
            tweet_db.twitter_user_screenname = current_user_tweet[ 'user' ][ 'screen_name' ]
            tweet_db.user_follower_count = current_user_tweet[ 'user' ][ 'followers_count' ]
            tweet_db.user_favorites_count = current_user_tweet[ 'user' ][ 'favourites_count' ]
            tweet_db.user_created = current_user_tweet[ 'user' ][ 'created_at' ]
    
            # save to database
            tweet_db.save()
    
        #-- END 
    
    #-- END loop over current user's tweets --#
    
#-- END loop over tweets --#