from __future__ import unicode_literals

# python imports
import datetime

# python 2 or 3
import six.moves.urllib.parse

# external package imports
import dateutil.parser
import pytz
import twitter

# django imports
from django.utils import timezone

# python_utilities
from python_utilities.django_utils.django_string_helper import DjangoStringHelper
from python_utilities.json.json_helper import JSONHelper

# tweetnet
import tweetnet.models

'''
Sample tweet JSON - 2015-02-08
{
    "contributors": null,
    "coordinates": null,
    "created_at": "Sun Feb 08 17:19:39 +0000 2015",
    "entities": {
        "hashtags": [],
        "symbols": [],
        "trends": [],
        "urls": [
            {
                "display_url": "knzmuslim.com",
                "expanded_url": "http://knzmuslim.com",
                "indices": [
                    72,
                    94
                ],
                "url": "http://t.co/sfymYu8CVj"
            }
        ],
        "user_mentions": []
    },
    "favorite_count": 0,
    "favorited": false,
    "filter_level": "low",
    "geo": null,
    "id": 564473647612841985,
    "id_str": "564473647612841985",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "lang": "ar",
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 0,
    "retweeted": false,
    "source": "<a href=\"http://knzmuslim.com\" rel=\"nofollow\">knzmuslim \u0643\u0646\u0632 \u0627\u0644\u0645\u0633\u0644\u0645</a>",
    "text": "\u0627\u0644\u0644\u0647\u0645 \u0635\u0628\u062d\u0646\u0627 \u0628\u0645\u0627 \u064a\u0633\u0631\u0646\u0627 \u0648\u0643\u0641 \u0639\u0646\u0627 \u0645\u0627 \u064a\u0636\u0631\u0646\u0627 \u0648\u064a\u0633\u0631 \u0644\u0646\u0627 \u062f\u0631\u0648\u0628\u0646\u0627 \u0648\u0646\u0648\u0631 \u0628\u0646\u0648\u0631\u0643 \u064a\u0648\u0645\u0646\u0627 http://t.co/sfymYu8CVj",
    "timestamp_ms": "1423415979661",
    "truncated": false,
    "user": {
        "contributors_enabled": false,
        "created_at": "Tue Aug 05 08:20:21 +0000 2014",
        "default_profile": true,
        "default_profile_image": false,
        "description": "\u0635\u0646\u0627\u0639 \u0627\u0644\u062d\u064a\u0627\u0647",
        "favourites_count": 0,
        "follow_request_sent": null,
        "followers_count": 24,
        "following": null,
        "friends_count": 37,
        "geo_enabled": false,
        "id": 2708736350,
        "id_str": "2708736350",
        "is_translator": false,
        "lang": "ar",
        "listed_count": 0,
        "location": "",
        "name": " \u0644\u064a\u0646\u0627 \u0627\u062d\u0645\u062f",
        "notifications": null,
        "profile_background_color": "C0DEED",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
        "profile_background_tile": false,
        "profile_image_url": "http://pbs.twimg.com/profile_images/496571979177017345/bSFdCKPp_normal.jpeg",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/496571979177017345/bSFdCKPp_normal.jpeg",
        "profile_link_color": "0084B4",
        "profile_sidebar_border_color": "C0DEED",
        "profile_sidebar_fill_color": "DDEEF6",
        "profile_text_color": "333333",
        "profile_use_background_image": true,
        "protected": false,
        "screen_name": "linaa_hmad",
        "statuses_count": 7045,
        "time_zone": null,
        "url": null,
        "utc_offset": null,
        "verified": false
    }
}

''' 

# declare variables
my_oauth = None
twitter_stream = None
tweet_iterator = None
tweet_counter = 0
current_tweet = None
delete_info = None
current_tweet_JSON_string = ""
tweet_db = None
tweet_create_dt = None
tweet_user_create_dt = None

# hashtag processing
tweet_hashtag_json_list = None
hashtag_count = -1
tweet_hashtag_json = None
current_hashtag_text = ""
tweet_hashtag_list = []

# url processing
tweet_url_json_list = None
url_count = -1
tweet_url_json = None
current_url_text = ""
current_dislpay_url_text = ""
current_short_url_text = ""
tweet_url_list = []
tweet_display_url_list = []
tweet_short_url_list = []

# user mention processing
tweet_user_mentions_json_list = None
user_mention_count = -1
tweet_user_mention_json = None
current_user_id = ""
current_user_screenname = ""
tweet_user_id_list = []
tweet_user_screenname_list = []

# save JSON?
do_save_json_to_database = True
tweet_json = None

# set up OAuth stuff.
CONSUMER_KEY = 'udM75GE2UgNs6dc58V8J2A'
CONSUMER_SECRET = 'XDBr3FniFvGCPGB4txgdqeyR9QWdqSCpj7cxyETPzPA'
ACCESS_KEY = '16529583-6no9QAZ8XYhI3i8w3PilTLt8GnylgmeYxOk8BOiCa'
ACCESS_SECRET = 'Wjp64PhlVciKmNgypqYaKbHHgyaHpFZLRYdXdowk'

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

    tweet_counter += 1
    
    # check for delete request.
    try:
    
        # if delete request, will have a delete element at the root.
        # If not, this will throw an exception, and you'll process the tweet.
        delete_info = current_tweet[ 'delete' ]
        print( "--> Deletion request - moving on." )
    
    except:

        # print out the tweet.
        #print( "====> Tweet JSON:" )
        #print( current_tweet_JSON_string )

        #------------------------------------------------------------------------
        # tweet data
        #------------------------------------------------------------------------

        # create a tweet object.
        tweet_db = tweetnet.models.Tweet()
        tweet_db.twitter_tweet_id = current_tweet[ 'id' ]
        tweet_db.tweet_text = DjangoStringHelper.encode_string( current_tweet[ 'text' ], entitize_4_byte_unicode_IN = True )
        tweet_db.tweet_timestamp = current_tweet[ 'created_at' ]
        
        # make timezone aware (all twitter dates are UTC)
        #tweet_create_dt = datetime.datetime.strptime( tweet_db.tweet_timestamp, tweetnet.models.TWITTER_DATE_FORMAT )
        #tweet_db.tweet_timestamp_dt = pytz.utc.localize( tweet_create_dt, is_dst = None )
        
        # try dateutil's parser
        tweet_db.tweet_timestamp_dt = dateutil.parser.parse( tweet_db.tweet_timestamp )
        
        tweet_db.timestamp_year = tweet_db.tweet_timestamp_dt.year
        tweet_db.timestamp_month = tweet_db.tweet_timestamp_dt.month
        tweet_db.timestamp_day = tweet_db.tweet_timestamp_dt.day
        tweet_db.timestamp_hour = tweet_db.tweet_timestamp_dt.hour
        tweet_db.timestamp_minute = tweet_db.tweet_timestamp_dt.minute
        tweet_db.timestamp_second = tweet_db.tweet_timestamp_dt.second
        tweet_db.timestamp_ms = [ 'timestamp_ms' ]
        tweet_db.tweet_language = current_tweet[ 'lang' ]
        tweet_db.tweet_place = current_tweet[ 'place' ]
        tweet_db.tweet_retweet_count = current_tweet[ 'retweet_count' ]
        tweet_db.tweet_geo = current_tweet[ 'geo' ]
        
        # !tweet hashtags?
        tweet_hashtag_json_list = current_tweet[ 'entities' ][ 'hashtags' ]
        hashtag_count = len( tweet_hashtag_json_list )
        if hashtag_count > 0:
        
            # got at least one hashtag. loop and build list.
            tweet_hashtag_list = []
            for tweet_hashtag_json in tweet_hashtag_json_list:
            
                # get hash tag value
                current_hashtag_text = tweet_hashtag_json[ 'text' ]
                
                # append to list
                tweet_hashtag_list.append( current_hashtag_text )
            
            #-- END loop over hash tags --#
        
            # store count
            tweet_db.tweet_hashtag_mention_count = len( tweet_hashtag_list )

            # convert to comma-delimited list for storage.
            tweet_db.tweet_hashtags_mentioned = ",".join( tweet_hashtag_list )

        #-- END check to see if one or more hash tags --#
        
        # !tweet urls?
        tweet_url_json_list = current_tweet[ 'entities' ][ 'urls' ]
        url_count = len( tweet_url_json_list )
        if url_count > 0:
        
            # got at least one url. loop and build lists.
            tweet_url_list = []
            tweet_display_url_list = []
            tweet_short_url_list = []
            for tweet_url_json in tweet_url_json_list:
            
                # get URL, display URL, and short URL
                current_url_text = tweet_url_json[ 'expanded_url' ]
                current_display_url_text = tweet_url_json[ 'display_url' ]
                current_short_url_text = tweet_url_json[ 'url' ]

                # append to lists
                encoded_value = current_url_text.encode( 'utf-8' )
                tweet_url_list.append( six.moves.urllib.parse.quote_plus( encoded_value ) )
                encoded_value = current_display_url_text.encode( 'utf-8' )
                tweet_display_url_list.append( six.moves.urllib.parse.quote_plus( encoded_value ) )
                encoded_value = current_short_url_text.encode( 'utf-8' )
                tweet_short_url_list.append( six.moves.urllib.parse.quote_plus( encoded_value ) )
            
            #-- END loop over URLs --#
        
            # store count
            tweet_db.tweet_url_count = len( tweet_url_list )

            # convert to comma-delimited lists for storage.
            tweet_db.tweet_shortened_urls_mentioned = ",".join( tweet_short_url_list )
            tweet_db.tweet_display_urls_mentioned = ",".join( tweet_display_url_list )
            tweet_db.tweet_full_urls_mentioned = ",".join( tweet_url_list )

        #-- END check to see if one or more urls --#
        
        # !tweet user mentions?
        tweet_user_mentions_json_list = current_tweet[ 'entities' ][ 'user_mentions' ]
        user_mention_count = len( tweet_user_mentions_json_list )
        if user_mention_count > 0:
        
            # got at least one user mention. loop and build lists.
            tweet_user_id_list = []
            tweet_user_screenname_list = []
            for tweet_user_mention_json in tweet_user_mentions_json_list:
            
                # get user mention values
                current_user_id = tweet_user_mention_json[ 'id_str' ]
                current_user_screenname = tweet_user_mention_json[ 'screen_name' ]
                
                # append to lists
                tweet_user_id_list.append( current_user_id )
                tweet_user_screenname_list.append( current_user_screenname )
            
            #-- END loop over hash tags --#
        
            # store count
            tweet_db.tweet_user_mention_count = len( tweet_user_id_list )

            # convert to comma-delimited lists for storage.
            tweet_db.tweet_users_mentioned_ids = ",".join( tweet_user_id_list )
            tweet_db.tweet_users_mentioned_screennames = ",".join( tweet_user_screenname_list )

        #-- END check to see if one or more user mentions --#
        
        #------------------------------------------------------------------------
        # user data
        #------------------------------------------------------------------------

        tweet_db.twitter_user_twitter_id = current_tweet[ 'user' ][ 'id' ]
        tweet_db.twitter_user_screenname = current_tweet[ 'user' ][ 'screen_name' ]
        tweet_db.user_followers_count = current_tweet[ 'user' ][ 'followers_count' ]
        tweet_db.user_favorites_count = current_tweet[ 'user' ][ 'favourites_count' ]
        tweet_db.user_friends_count = current_tweet[ 'user' ][ 'friends_count' ]
        tweet_db.user_created = current_tweet[ 'user' ][ 'created_at' ]
        
        # created_at datetime - make time-zone aware
        #tweet_user_create_dt = datetime.datetime.strptime( tweet_db.user_created, tweetnet.models.TWITTER_DATE_FORMAT )
        #tweet_db.user_created_dt = pytz.utc.localize( tweet_user_create_dt, is_dst = None )
        
        # try dateutil's parser
        tweet_db.user_created_dt = dateutil.parser.parse( tweet_db.user_created )
        
        tweet_db.user_location = current_tweet[ 'user' ][ 'location' ]
        tweet_db.user_description = current_tweet[ 'user' ][ 'description' ]
        tweet_db.user_statuses_count = current_tweet[ 'user' ][ 'statuses_count' ]

        # save to database
        tweet_db.save()
        
        #------------------------------------------------------------------------
        # JSON
        #------------------------------------------------------------------------

        # save JSON to database?
        if do_save_json_to_database == True:

            tweet_json = tweetnet.models.Tweet_JSON()
            tweet_json.tweet = tweet_db
            
            # convert JSON to pretty-printed string
            current_tweet_JSON_string = JSONHelper.pretty_print_json( current_tweet )
            
            # store JSON string
            tweet_json.tweet_json = current_tweet_JSON_string
    
            # save to database.
            tweet_json.save()
            
        #-- END check to see if we save JSON to database --#

    #-- END try-except to see if deleted tweet. --#
    
    if ( tweet_counter % 100 ) == 0:
    
        # yes - print a brief message
        print( "====> tweet count = " + str( tweet_counter ) )
    
    #-- END check to see if we've done another hundred --#
    
#-- END loop over tweet stream --#