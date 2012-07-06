# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Tweet( models.Model ):

    tweet_timestamp = models.CharField( max_length = 255, blank = True )
    tweet_timestamp_datetime = models.DateTimeField( null = True, blank = True )
    twitter_tweet_id = models.BigIntegerField()
    twitter_user = models.ForeignKey( 'Twitter_User' )
    twitter_user_screenname = models.CharField( max_length = 255 )
    tweet_retweet_count = models.IntegerField( null = True, blank = True )
    tweet_location = models.TextField( null = True, blank = True )
    tweet_has_location = models.IntegerField( null = True, blank = True )
    user_follower_count = models.IntegerField( null = True, blank = True )
    user_favorites_count = models.IntegerField( null = True, blank = True )
    user_created = models.CharField( max_length = 255, blank = True )
    user_created_datetime = models.DateTimeField( null = True, blank = True )
    user_location = models.TextField( null = True, blank=True )
    tweet_user_mention_count = models.IntegerField( null = True, blank = True )
    tweet_users_mentioned = models.TextField( null = True, blank = True )
    tweet_users_mentioned_ids = models.TextField( null = True, blank = True )
    tweet_hashtag_mention_count = models.IntegerField( null = True, blank = True )
    tweet_hashtags_mentioned = models.TextField( null = True, blank = True )
    tweet_url_count = models.IntegerField( null = True, blank = True )
    tweet_full_urls_mentioned = models.TextField( null = True, blank = True )
    tweet_text_length = models.IntegerField( null = True, blank = True )
    tweet_text = models.TextField( null = True, blank = True )
    outlet_label = models.CharField( max_length = 255, blank = True )
    outlet_id = models.IntegerField( null = True, blank = True )
    is_bbc = models.IntegerField( null = True, blank = True )
    is_cbs = models.IntegerField( null = True, blank = True )
    is_cnn = models.IntegerField( null = True, blank = True )
    is_drudge = models.IntegerField( null = True, blank = True )
    is_fox = models.IntegerField( null = True, blank = True )
    is_huffington = models.IntegerField( null = True, blank = True )
    is_msnbc = models.IntegerField( null = True, blank = True )
    is_nyt = models.IntegerField( null = True, blank = True )
    is_npr = models.IntegerField( null = True, blank = True )
    is_usatoday = models.IntegerField( null = True, blank = True )
    is_wsj = models.IntegerField( null = True, blank = True )
    is_wpo = models.IntegerField( null = True, blank = True )
    ideology = models.CharField( max_length = 255, blank = True )
    is_liberal = models.IntegerField( null = True, blank = True )
    is_conservative = models.IntegerField( null = True, blank = True )
    is_control = models.IntegerField( null = True, blank = True )
    ideology_int = models.IntegerField( null = True, blank = True )
    heterogeneity = models.CharField( max_length = 255, blank = True )
    is_low_h = models.IntegerField( null = True, blank = True )
    is_medium_h = models.IntegerField( null = True, blank = True )
    is_high_h = models.IntegerField( null = True, blank = True )
    heterogeneity_int = models.IntegerField( null = True, blank = True )
    timestamp_year = models.IntegerField( null = True, blank = True )
    timestamp_month = models.IntegerField( null = True, blank = True )
    timestamp_day = models.IntegerField( null = True, blank = True )
    timestamp_hour = models.IntegerField( null = True, blank = True )
    timestamp_minute = models.IntegerField( null = True, blank = True )
    timestamp_second = models.IntegerField( null = True, blank = True )

    #----------------------------------------------------------------------
    # instance methods
    #----------------------------------------------------------------------

    def __unicode__( self ):
 
        # return reference
        string_OUT = ''
 
        if ( self.id ):
        
            string_OUT = str( self.id ) + " - "
            
        #-- END check to see if ID --#
                
        string_OUT += self.twitter_tweet_id
        
        # screenname?
        if ( self.twitter_user_screenname ):
        
            string_OUT += " ( " + self.twitter_user_screenname
            
            # link to Twitter_User?
            if ( self.twitter_user ):
            
                # yes.  Output ID.
                string_OUT += " - " + self.twitter_user.id
            
            #-- END check to see if twitter user. --#
            
            string_OUT += " )"
            
        #-- END screenname check --#

        if ( self.tweet_text ):
        
            string_OUT += + ": " + self.tweet_text
            
        #-- END check to see if we have tweet text. --#
 
        return string_OUT

    #-- END method __unicode__() --#

#-- END class Tweet --#


class Twitter_User( models.Model ):

    twitter_user_name = models.CharField( max_length = 255, blank=True )
    tweet_count = models.IntegerField( null = True, blank = True )
    tweet_retweet_count_mean = models.FloatField( null = True, blank = True )
    tweet_retweet_count_sum = models.IntegerField( null = True, blank = True )
    user_follower_count_max = models.IntegerField( null = True, blank = True )
    user_favorites_count_max = models.IntegerField( null = True, blank = True )
    tweet_user_mention_count_mean = models.FloatField( null = True, blank = True )
    tweet_user_mention_count_sum = models.IntegerField( null = True, blank = True )
    tweet_hashtag_mention_count_mean = models.FloatField( null = True, blank = True )
    tweet_hashtag_mention_count_sum = models.IntegerField( null = True, blank = True )
    tweet_url_count_mean = models.FloatField( null = True, blank = True )
    tweet_url_count_sum = models.IntegerField( null = True, blank = True )
    tweet_text_length_mean_1 = models.FloatField( null = True, blank = True )
    tweet_text_length_median = models.FloatField( null = True, blank = True )
    is_bbc_sum = models.IntegerField( null = True, blank = True )
    is_cbs_sum = models.IntegerField( null = True, blank = True )
    is_cnn_sum = models.IntegerField( null = True, blank = True )
    is_drudge_sum = models.IntegerField( null = True, blank = True )
    is_fox_sum = models.IntegerField( null = True, blank = True )
    is_huffington_sum = models.IntegerField( null = True, blank = True )
    is_msnbc_sum = models.IntegerField( null = True, blank = True )
    is_nyt_sum = models.IntegerField( null = True, blank = True )
    is_npr_sum = models.IntegerField( null = True, blank = True )
    is_usatoday_sum = models.IntegerField( null = True, blank = True )
    is_wsj_sum = models.IntegerField( null = True, blank = True )
    is_wpo_sum = models.IntegerField( null = True, blank = True )
    is_liberal_sum = models.IntegerField( null = True, blank = True )
    is_control_sum = models.IntegerField( null = True, blank = True )
    is_conservative_sum = models.IntegerField( null = True, blank = True )
    outlet_heterogeneity_low_sum = models.IntegerField( null = True, blank = True )
    outlet_heterogeneity_med_sum = models.IntegerField( null = True, blank = True )
    outlet_heterogeneity_high_sum = models.IntegerField( null = True, blank = True )
    is_bbc_max = models.IntegerField( null = True, blank = True )
    is_cbs_max = models.IntegerField( null = True, blank = True )
    is_cnn_max = models.IntegerField( null = True, blank = True )
    is_drudge_max = models.IntegerField( null = True, blank = True )
    is_fox_max = models.IntegerField( null = True, blank = True )
    is_huffington_max = models.IntegerField( null = True, blank = True )
    is_msnbc_max = models.IntegerField( null = True, blank = True )
    is_nyt_max = models.IntegerField( null = True, blank = True )
    is_npr_max = models.IntegerField( null = True, blank = True )
    is_usatoday_max = models.IntegerField( null = True, blank = True )
    is_wsj_max = models.IntegerField( null = True, blank = True )
    is_wpo_max = models.IntegerField( null = True, blank = True )
    diversity = models.FloatField( null = True, blank = True )
    ideology_count = models.IntegerField( null = True, blank = True )
    ideology_code = models.IntegerField( null = True, blank = True )

    #----------------------------------------------------------------------
    # instance methods
    #----------------------------------------------------------------------

    def __unicode__( self ):
 
        # return reference
        string_OUT = ''
 
        if ( self.id ):
        
            string_OUT = str( self.id ) + " - "
            
        #-- END check to see if ID --#
                
        # screenname?
        if ( self.twitter_user_name ):
        
            string_OUT += self.twitter_user_name
            
        #-- END screenname check --#

        return string_OUT

    #-- END method __unicode__() --#

#-- END class Twitter_User --#