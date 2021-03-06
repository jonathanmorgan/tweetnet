#==============================================================================#
# imports
#==============================================================================#

from __future__ import unicode_literals

# Python base packages
import gc
import json
import sys
import traceback

# Email imports
import smtplib

# MIME types for emails
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# import six python 2-3 compatibility package
import six

# import twitter
import twitter

# import MySQL database package
import MySQLdb

#==============================================================================#
# functions
#==============================================================================#


def get_dict_value( dict_IN, name_IN, default_IN = "", convert_None_to_IN = None ):

    '''
    Accepts dictionary, name of property in dict we want to retrieve, default
       value used if name not present, and value we want None converted to if
       it is returned.
    '''
    
    # return reference
    value_OUT = None
    
    # try retrieving using .get()
    value_OUT = dict_IN.get( name_IN, default_IN )
    
    # is value None?
    if ( value_OUT == None ):

        # is convert_None_to_IN something other than None?
        if ( convert_None_to_IN is not None ):
        
            # it is other than None.  Return that instead.
            value_OUT = convert_None_to_IN
        
        #-- END check to see if we convert from None to something else. --#
        
    #-- END check to see if value_OUT is None --#
    
    return value_OUT

#-- END function get_dict_value() --#


def send_email( email_message_body_IN = "Empty message body.",
                email_subject_IN = "Empty message subject.",
                email_from_IN = "",
                email_to_IN = "",
                smtp_use_ssl_IN = True,
                smtp_host_IN = "localhost",
                smtp_port_IN = -1,
                smtp_username_IN = "",
                smtp_password_IN = "" ):

    # declare variables
    email_message = None
    my_smtp_server = None
    
    # create MIME email message
    email_message = MIMEText( email_message_body_IN )
    email_message[ 'Subject' ] = email_subject_IN
    email_message[ 'From' ] = email_from_IN
    email_message[ 'To' ] = email_to_IN
    
    # use SSL?
    if ( smtp_use_ssl_IN == True ):

        # use SSL - got port?
        if ( ( smtp_port_IN is not None ) and ( smtp_port_IN != "" ) and ( smtp_port_IN > 0 ) ):

            # yes
            my_smtp_server = smtplib.SMTP_SSL( smtp_host_IN, smtp_port_IN )
            
        else:
        
            # no
            my_smtp_server = smtplib.SMTP_SSL( smtp_host_IN )
            
        #-- END check to see if port. --#
        
    else:
    
        # don't use SSL - got port?
        if ( ( smtp_port_IN is not None ) and ( smtp_port_IN != "" ) and ( smtp_port_IN > 0 ) ):

            # yes
            my_smtp_server = smtplib.SMTP( smtp_host_IN, smtp_port_IN )
            
        else:
        
            # no
            my_smtp_server = smtplib.SMTP( smtp_host_IN )
            
        #-- END check to see if port. --#
        
    #-- END check to see if use SSL --#
    
    # got username (allow empty password)?
    if ( ( smtp_username_IN ) and ( smtp_username_IN != None ) and ( smtp_username_IN != "" ) ):
    
        # yes.  Login.
        my_smtp_server.login( smtp_username_IN, smtp_password_IN )
        
    #-- END check to see if we have username. --#

    # send email
    my_smtp_server.sendmail( email_from_IN, email_to_IN, email_message.as_string() )
    my_smtp_server.quit()

#-- END function send_email() --#


#==============================================================================#
# declare variables
#==============================================================================#

# variables to hold tweet info for "raw" table
tweet_timestamp = ""
twitter_tweet_id = ""
tweet_text = ""
tweet_language = ""
tweet_retweet_count = ""
tweet_place = ""
tweet_user_mention_count = ""
tweet_users_mentioned_screennames = ""
tweet_users_mentioned_ids = ""
tweet_hashtag_mention_count = ""
tweet_hashtags_mentioned = ""
tweet_url_count = ""
tweet_shortened_urls_mentioned = ""
tweet_full_urls_mentioned = ""
tweet_display_urls_mentioned = ""
timestamp_ms = ""
tweet_geo = ""
twitter_user_twitter_id = ""
twitter_user_screenname = ""
user_followers_count = ""
user_favorites_count = ""
user_friends_count = ""
user_created = ""
user_location = ""
user_description = ""
user_statuses_count = ""

# variables for processing tweets
keep_trying = True
stop_count = -1
stop_limit = 10
exception_count = -1
exception_limit = 10
my_oauth = None
twitter_stream = None
tweet_iterator = None
tweet_counter = -1
current_tweet = None
tweet_hangup = False
tweet_heartbeat_timeout = False
exception_in_loop = False

# JSON processing
current_tweet_entities = None
current_tweet_user = None
tweet_place_JSON = None
do_save_json_to_database = False
current_tweet_JSON_string = ""
coordinates_dict = None
coordinates_list = None
coordinates_longitude = -1
coordinates_latitude = -1

# variables for database interaction
db_username = ""
db_password = ""
db_database = ""
db_connection = None
db_cursor = None
db_insert_value_tuple = None
sql_insert_string = ""
db_tweet_id = -1
sql_json_insert_string = ""

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
current_display_url_text = ""
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

# variables for emailing on error.
smtp_host = ""
smtp_port = -1
smtp_username = ""
smtp_password = ""
smtp_use_ssl = True
email_subject = ""
email_from = ""
email_to = ""
email_message = None
email_message_body = ""

#==============================================================================#
# configuration
#==============================================================================#

# set up database connection.
db_username = ""
db_password = ""
db_database = ""

# set up OAuth stuff.
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''
    
# configure SMTP, for use when there is an exception.
smtp_host = ""
smtp_port = 465
smtp_username = ""
smtp_password = ""
smtp_use_ssl = True
email_from = "" # can be different from SMTP user
email_to = ""

#==============================================================================#
# program logic
#==============================================================================#

# define SQL statements here, once, rather than each time through the loop.

#== tweetnet_tweet_download_raw ==#
sql_insert_string = '''
    INSERT INTO tweetnet_tweet_download_raw
    (
        tweet_timestamp,
        twitter_tweet_id,
        tweet_text,
        tweet_language,
        tweet_retweet_count,
        tweet_place,
        tweet_user_mention_count,
        tweet_users_mentioned_screennames,
        tweet_users_mentioned_ids,
        tweet_hashtag_mention_count,
        tweet_hashtags_mentioned,
        tweet_url_count,
        tweet_shortened_urls_mentioned,
        tweet_full_urls_mentioned,
        tweet_display_urls_mentioned,
        timestamp_ms,
        tweet_geo,
        twitter_user_twitter_id,
        twitter_user_screenname,
        user_followers_count,
        user_favorites_count,
        user_friends_count,
        user_created,
        user_location,
        user_description,
        user_statuses_count
    )
    VALUES
    (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    )
'''

#== tweetnet_tweet_json ==#
sql_json_insert_string = '''
    INSERT INTO tweetnet_tweet_json
    (
        tweet_json,
        twitter_tweet_id
    )
    VALUES
    (
        %s,
        %s
    )
'''

# connect inside try, in case connection fails.
try:

    # Create database connection
    db_connection = MySQLdb.connect( user = db_username, passwd = db_password, db = db_database )

    # create mysql cursor that maps column names to values in the query result.
    db_cursor = db_connection.cursor( MySQLdb.cursors.DictCursor )
    
    # !make a loop here, keep reconnecting...
    stop_count = 0
    exception_count = 0
    while keep_trying == True:

        try:

            # Make an OAuth object.
            my_oauth = twitter.OAuth( ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET )
            
            # Create a tweetstream
            twitter_stream = twitter.TwitterStream( auth = my_oauth )
            
            # get an iterator over tweets - basic sample
            tweet_iterator = twitter_stream.statuses.sample()
            
            # or, filtered sample
            # from https://dev.twitter.com/streaming/reference/post/statuses/filter
            # "track" = list of string keywords
            # "locations" = list of string lat. long. locations ( "<lat>,<long>" )
            # "follow" = list of users whose statuses we want returned.
            #tweet_iterator = twitter_stream.statuses.filter( track = [ "nytimes", ] )
            
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
                    
                    # Per Python "twitter" documentation ():
                    # "The iterator will yield until the TCP connection breaks. When the
                    #    connection breaks, the iterator yields: {'hangup': True}, and
                    #    raises StopIteration if iterated again.
                    #
                    # Similarly, if the stream does not produce heartbeats for more than
                    #    90 seconds, the iterator yields:
                    #    {'hangup': True, 'heartbeat_timeout': True}, and raises
                    #    StopIteration if iterated again.
                    
                    # try to get "hangup", "heartbeat_timeout"
                    tweet_hangup = current_tweet.get( "hangup", False )
                    tweet_heartbeat_timeout = current_tweet.get( "heartbeat_timeout", False )
                    
                    # got either of these indicators of a stop?
                    if ( ( tweet_hangup == True ) or ( tweet_heartbeat_timeout == True ) ):
                    
                        # we do.  Appears our connection has closed.  Increment
                        #    stop_count, then email.
                        stop_count += 1
                        
                        # build message
                        email_message_body = "TweetStream created JSON object that indicates that we've been cut off.  Stop count = " + str( stop_count ) + ".  JSON object:\n\n"
                        email_message_body += json.dumps( current_tweet, sort_keys = True, indent = 4, separators = ( ',', ': ' ) )
                        
                        send_email( email_message_body_IN = email_message_body,
                            email_subject_IN = "[UMD] - TweetStream has been cut off.",
                            email_from_IN = email_from,
                            email_to_IN = email_to,
                            smtp_use_ssl_IN = smtp_use_ssl,
                            smtp_host_IN = smtp_host,
                            smtp_port_IN = smtp_port,
                            smtp_username_IN = smtp_username,
                            smtp_password_IN = smtp_password )
                            
                        # output message
                        print( email_message_body )
        
                    else:
            
                        #------------------------------------------------------------------------
                        # tweet data
                        #------------------------------------------------------------------------
                
                        # get tweet data
                        tweet_timestamp = get_dict_value( current_tweet, 'created_at', "", "" )
                        twitter_tweet_id = get_dict_value( current_tweet, 'id', "", "" )
                        tweet_text = get_dict_value( current_tweet, 'text', "", "" )
                        tweet_language = get_dict_value( current_tweet, 'lang', "", "" )
                        tweet_retweet_count = get_dict_value( current_tweet, 'retweet_count', "", "" )
                        
                        # init tweet_place to empty
                        tweet_place = ""
                        
                        # check if tweet place in JSON
                        tweet_place_JSON = current_tweet.get( 'place' )
                        if ( ( tweet_place_JSON is not None) and ( tweet_place_JSON != "" ) ):
                
                            # got JSON - get full_name from inside.
                            tweet_place = get_dict_value( tweet_place_JSON, "full_name", "", "" )
                
                        else:
                            
                            # no place.
                            tweet_place = ""
                            
                        #-- END check to see if tweet_place present --#
                
                        # !tweet user mentions?
                        
                        # initialize user mention variables.
                        tweet_user_mention_count = 0
                        tweet_users_mentioned_ids = ""
                        tweet_users_mentioned_screennames = ""
                        
                        # entities
                        current_tweet_entities = current_tweet.get( 'entities' )
                        if ( current_tweet_entities is not None ):
                            
                            # do we have user mentions in this tweet?
                            tweet_user_mentions_json_list = current_tweet_entities.get( 'user_mentions' )
                            user_mention_count = len( tweet_user_mentions_json_list )
                            if user_mention_count > 0:
                            
                                # got at least one user mention. loop and build lists.
                                tweet_user_id_list = []
                                tweet_user_screenname_list = []
                                for tweet_user_mention_json in tweet_user_mentions_json_list:
                                
                                    # get user mention values
                                    current_user_id = get_dict_value( tweet_user_mention_json, 'id_str', "", "" )
                                    current_user_screenname = get_dict_value( tweet_user_mention_json, 'screen_name', "", "" )
                                    
                                    # append to lists
                                    tweet_user_id_list.append( current_user_id )
                                    tweet_user_screenname_list.append( current_user_screenname )
                                
                                #-- END loop over hash tags --#
                            
                                # store count
                                tweet_user_mention_count = len( tweet_user_id_list )
                    
                                # convert to comma-delimited lists for storage.
                                tweet_users_mentioned_ids = ",".join( tweet_user_id_list )
                                tweet_users_mentioned_screennames = ",".join( tweet_user_screenname_list )
                    
                            else:
                                
                                # no user mentions - set count to 0, everything else to "".
                                tweet_user_mention_count = 0
                                tweet_users_mentioned_ids = ""
                                tweet_users_mentioned_screennames = ""
                                
                            #-- END check to see if one or more user mentions --#
                            
                            # !tweet hashtags?
                            
                            # initialize hashtag variables
                            tweet_hashtag_mention_count = 0
                            tweet_hashtags_mentioned = ""
                            
                            # see if we have any hash tags
                            tweet_hashtag_json_list = current_tweet_entities.get( 'hashtags' )
                            hashtag_count = len( tweet_hashtag_json_list )
                            if hashtag_count > 0:
                            
                                # got at least one hashtag. loop and build list.
                                tweet_hashtag_list = []
                                for tweet_hashtag_json in tweet_hashtag_json_list:
                                
                                    # get hash tag value
                                    current_hashtag_text = get_dict_value( tweet_hashtag_json, 'text', "", "" )
                                    
                                    # append to list
                                    tweet_hashtag_list.append( current_hashtag_text )
                                
                                #-- END loop over hash tags --#
                            
                                # store count
                                tweet_hashtag_mention_count = len( tweet_hashtag_list )
                    
                                # convert to comma-delimited list for storage.
                                tweet_hashtags_mentioned = ",".join( tweet_hashtag_list )
                    
                            else:
                                
                                # set all variables to 0, empty string.
                                tweet_hashtag_mention_count = 0
                                tweet_hashtags_mentioned = ""
                                
                            #-- END check to see if one or more hash tags --#
                            
                            # !tweet urls?
                            
                            # initialize URL variables.
                            tweet_url_count = 0
                            tweet_shortened_urls_mentioned = ""
                            tweet_display_urls_mentioned = ""
                            tweet_full_urls_mentioned = ""
                    
                            # do we have URLs in tweet?
                            tweet_url_json_list = current_tweet_entities.get( 'urls' )
                            url_count = len( tweet_url_json_list )
                            if url_count > 0:
                            
                                # got at least one url. loop and build lists.
                                tweet_url_list = []
                                tweet_display_url_list = []
                                tweet_short_url_list = []
                                for tweet_url_json in tweet_url_json_list:
                                
                                    # get URL, display URL, and short URL
                                    current_url_text = get_dict_value( tweet_url_json, 'expanded_url', "", "" )
                                    current_display_url_text = get_dict_value( tweet_url_json, 'display_url', "", "" )
                                    current_short_url_text = get_dict_value( tweet_url_json, 'url', "", "" )
                    
                                    # append to lists
                                    encoded_value = current_url_text.encode( 'utf-8' )
                                    tweet_url_list.append( six.moves.urllib.parse.quote_plus( encoded_value ) )
                                    encoded_value = current_display_url_text.encode( 'utf-8' )
                                    tweet_display_url_list.append( six.moves.urllib.parse.quote_plus( encoded_value ) )
                                    encoded_value = current_short_url_text.encode( 'utf-8' )
                                    tweet_short_url_list.append( six.moves.urllib.parse.quote_plus( encoded_value ) )
                                
                                #-- END loop over URLs --#
                            
                                # store count
                                tweet_url_count = len( tweet_url_list )
                    
                                # convert to comma-delimited lists for storage.
                                tweet_shortened_urls_mentioned = ",".join( tweet_short_url_list )
                                tweet_display_urls_mentioned = ",".join( tweet_display_url_list )
                                tweet_full_urls_mentioned = ",".join( tweet_url_list )
                    
                            else:
                                
                                # set count to 0, everything else to "".
                                tweet_url_count = 0
                                tweet_shortened_urls_mentioned = ""
                                tweet_display_urls_mentioned = ""
                                tweet_full_urls_mentioned = ""
                                
                            #-- END check to see if one or more urls --#
                            
                        #-- END check to see if entities present. --#
                        
                        timestamp_ms = get_dict_value( current_tweet, "timestamp_ms", "", "" )
                        
                        # check to see if we have geo information (now stored in
                        #    "coordinates").
                        tweet_geo = get_dict_value( current_tweet, "coordinates", "", "" )
            
                        # got geo dictionary?
                        if ( isinstance( tweet_geo, dict ) == True ):
                        
                            # yes - I'll be darned.  Example:
                            #    "coordinates":
                            #    {
                            #        "coordinates":
                            #        [
                            #            -75.14310264,
                            #            40.05701649
                            #        ],
                            #        "type":"Point"
                            #    }
                            # in "coordinates" list, long, then lat (GeoJSON - http://geojson.org/)
                            coordinates_dict = tweet_geo
                            coordinates_list = coordinates_dict.get( "coordinates", None )
                            if ( ( coordinates_list is not None ) and ( len( coordinates_list ) == 2 ) ):
                            
                                # Retrieve long and lat, combine into a string.
                                coordinates_longitude = coordinates_list[ 0 ]
                                coordinates_latitude = coordinates_list[ 1 ]
                                tweet_geo = str( coordinates_longitude ) + "," + str( coordinates_latitude )
            
                            else:
                            
                                # error - just store the whole thing as a string.
                                tweet_geo = str( coordinates_dict )
                                
                            #-- END check to see if 2 coordinates --#
                            
                        else:
                        
                            # not a dict - make sure it is "".
                            tweet_geo = ""
                            
                        #-- END check to see if coordinates --#
                                
                        #------------------------------------------------------------------------
                        # ! user data
                        #------------------------------------------------------------------------
                
                        twitter_user_twitter_id = ""
                        twitter_user_screenname = ""
                        user_followers_count = ""
                        user_favorites_count = ""
                        user_friends_count = ""
                        user_created = ""
                        user_location = ""
                        user_description = ""
                        user_statuses_count = ""
                
                        # get user
                        current_tweet_user = current_tweet.get( "user" )
                        
                        # got one?
                        if ( current_tweet_user is not None ):
                        
                            # get user information.
                            twitter_user_twitter_id = get_dict_value( current_tweet_user, 'id', "", "" )
                            twitter_user_screenname = get_dict_value( current_tweet_user, 'screen_name', "", "" )
                            user_followers_count = int( get_dict_value( current_tweet_user, 'followers_count', "0", "0" ) )
                            user_favorites_count = int( get_dict_value( current_tweet_user, 'favourites_count', "0", "0" ) )
                            user_friends_count = int( get_dict_value( current_tweet_user, 'friends_count', "0", "0" ) )
                            user_created = get_dict_value( current_tweet_user, 'created_at', "", "" )
                            user_location = get_dict_value( current_tweet_user, 'location', "", "" )
                            user_description = get_dict_value( current_tweet_user, 'description', "", "" )
                            user_statuses_count = int( get_dict_value( current_tweet_user, 'statuses_count', "0", "0" ) )
                            
                        #-- END user processing. --#
                
                        # DO SOMETHING WITH THE DATA!
                        #print( "--> " + str( twitter_tweet_id ) + " - " + tweet_text )
                    
                        # Insert the data into the tweetnet_tweet_download_raw table.
            
                        # execute the INSERT SQL command.
                        db_insert_value_tuple = (
                            tweet_timestamp.encode( 'utf-8' ),
                            twitter_tweet_id,
                            tweet_text.encode( 'utf-8' ),
                            tweet_language.encode( 'utf-8' ),
                            tweet_retweet_count,
                            tweet_place.encode( 'utf-8' ),
                            tweet_user_mention_count,
                            tweet_users_mentioned_screennames.encode( 'utf-8' ),
                            tweet_users_mentioned_ids.encode( 'utf-8' ),
                            tweet_hashtag_mention_count,
                            tweet_hashtags_mentioned.encode( 'utf-8' ),
                            tweet_url_count,
                            tweet_shortened_urls_mentioned.encode( 'utf-8' ),
                            tweet_full_urls_mentioned.encode( 'utf-8' ),
                            tweet_display_urls_mentioned.encode( 'utf-8' ),
                            timestamp_ms.encode( 'utf-8' ),
                            tweet_geo.encode( 'utf-8' ),
                            twitter_user_twitter_id,
                            twitter_user_screenname.encode( 'utf-8' ),
                            user_followers_count,
                            user_favorites_count,
                            user_friends_count,
                            user_created.encode( 'utf-8' ),
                            user_location.encode( 'utf-8' ),
                            user_description.encode( 'utf-8' ),
                            user_statuses_count
                        )
                        db_cursor.execute( sql_insert_string, db_insert_value_tuple )
                        db_connection.commit()
                        
                        # get ID of tweet just created
                        db_tweet_id = db_cursor.lastrowid
            
                        # save JSON to database?
                        if do_save_json_to_database == True:
                
                            # convert JSON to pretty-printed string
                            current_tweet_JSON_string = json.dumps( current_tweet, sort_keys = True, indent = 4, separators = ( ',', ': ' ) )
                            
                            # store JSON string - execute the INSERT SQL command.
                            db_insert_value_tuple = ( current_tweet_JSON_string.encode( 'utf-8' ), twitter_tweet_id )
                            db_cursor.execute( sql_json_insert_string, db_insert_value_tuple )
                            db_connection.commit()
                            
                        #-- END check to see if we save JSON to database --#
                        
                    #-- END check to see if we have been cut off from twitter --#
            
                #-- END try-except to see if deleted tweet. --#
                
                if ( tweet_counter % 100 ) == 0:
                
                    # yes - print a brief message
                    print( "====> tweet count = " + str( tweet_counter ) )
                    
                    # commit
                    #db_connection.commit()
                    
                    # collect garbage
                    gc.collect()
                
                #-- END check to see if we've done another hundred --#
                
            #-- END loop over tweet stream --#

        except Exception as e:

            # increment exception count, set flag.
            exception_count += 1
            exception_in_loop == True
            
            # get exception details
            exception_type, exception_value, exception_traceback = sys.exc_info()
            
            # Create exception message.
            email_message_body = "Exception caught inside \"keep_trying\" loop: "
            email_message_body += "\n- args = " + str( e.args )
            email_message_body += "\n- type = " + str( exception_type )
            email_message_body += "\n- value = " + str( exception_value )
            email_message_body += "\n- traceback = " + str( traceback.format_exc() )
        
            # email exception message
            send_email( email_message_body_IN = email_message_body,
                email_subject_IN = '[UMD] - Error in Twitter Collector inside \"keep_trying\" loop',
                email_from_IN = email_from,
                email_to_IN = email_to,
                smtp_use_ssl_IN = smtp_use_ssl,
                smtp_host_IN = smtp_host,
                smtp_port_IN = smtp_port,
                smtp_username_IN = smtp_username,
                smtp_password_IN = smtp_password )
        
            # output message
            print( email_message_body )
            
        #-- END TweetStream try/except --#

        # ! See if any errors.
        
        # did the stream stop on us?
        if ( ( tweet_hangup == True ) or ( tweet_heartbeat_timeout == True ) ):
        
            # stream stopped.  Keep trying until stop_count = stop_limit.
            if ( stop_count <= stop_limit ):
            
                # still under limit.
                keep_trying = True
                
            else:
            
                # at or over limit.  No more looping.
                keep_trying = False
            
                # build message
                email_message_body = "stop_count = stop_limit, so no longer trying to reconnect to Twitter streaming API.  Stop count = " + str( stop_count ) + "."
                
                send_email( email_message_body_IN = email_message_body,
                    email_subject_IN = "[UMD] - stop_count = stop_limit - TweetStream stopped.",
                    email_from_IN = email_from,
                    email_to_IN = email_to,
                    smtp_use_ssl_IN = smtp_use_ssl,
                    smtp_host_IN = smtp_host,
                    smtp_port_IN = smtp_port,
                    smtp_username_IN = smtp_username,
                    smtp_password_IN = smtp_password )
                    
                # output message
                print( email_message_body )

            #-- END check to see if we've reached stop_limit --#

        # or was there an exception thrown?
        elif exception_in_loop == True:
        
            # exception.  Keep trying until exception_count = exception_limit.
            if ( exception_count <= exception_limit ):
            
                # still under limit.
                keep_trying = True
                
            else:
            
                # at or over limit.  No more looping.
                keep_trying = False
            
                # build message
                email_message_body = "exception_count = exception_limit, so no longer trying to reconnect to Twitter streaming API.  Exception count = " + str( exception_count ) + "."
                
                send_email( email_message_body_IN = email_message_body,
                    email_subject_IN = "[UMD] - exception_count = exception_limit - TweetStream stopped.",
                    email_from_IN = email_from,
                    email_to_IN = email_to,
                    smtp_use_ssl_IN = smtp_use_ssl,
                    smtp_host_IN = smtp_host,
                    smtp_port_IN = smtp_port,
                    smtp_username_IN = smtp_username,
                    smtp_password_IN = smtp_password )
                    
                # output message
                print( email_message_body )

            #-- END check to see if we've reached stop_limit --#

        else:
        
            # TweetStream iteration stopped for some other reason...  Stop.
            keep_trying = False
        
            # build message
            email_message_body = "TweetStream processing ended, no exception or stop message.  Huh.  TweetStream stopped."
            
            send_email( email_message_body_IN = email_message_body,
                email_subject_IN = "[UMD] - TweetStream processing ended - TweetStream stopped.",
                email_from_IN = email_from,
                email_to_IN = email_to,
                smtp_use_ssl_IN = smtp_use_ssl,
                smtp_host_IN = smtp_host,
                smtp_port_IN = smtp_port,
                smtp_username_IN = smtp_username,
                smtp_password_IN = smtp_password )
                
            # output message
            print( email_message_body )

        #-- END check to see what we do next. --#
        
    #-- END "keep_trying" loop. --#

except Exception as e:

    # get exception details
    exception_type, exception_value, exception_traceback = sys.exc_info()
    
    # Create exception message.
    email_message_body = "Exception caught: "
    email_message_body += "\n- args = " + str( e.args )
    email_message_body += "\n- type = " + str( exception_type )
    email_message_body += "\n- value = " + str( exception_value )
    email_message_body += "\n- traceback = " + str( traceback.format_exc() )

    # email exception message
    send_email( email_message_body_IN = email_message_body,
        email_subject_IN = '[UMD] - Error in Twitter Collector',
        email_from_IN = email_from,
        email_to_IN = email_to,
        smtp_use_ssl_IN = smtp_use_ssl,
        smtp_host_IN = smtp_host,
        smtp_port_IN = smtp_port,
        smtp_username_IN = smtp_username,
        smtp_password_IN = smtp_password )

    # output message
    print( email_message_body )
    
finally:

    # close cursor
    if ( db_cursor is not None ):
    
        db_cursor.close()
        
    #-- END check to see if None --#

    # close database
    if ( db_connection is not None ):
    
        db_connection.close()
        
    #-- END check to see if None --#

#-- END try/except/finally around MySQL connection.