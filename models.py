from django.db import models

# not abstract for now.
# class Abstract_Tweet( models.Model ):
class Tweet( models.Model ):

    # timestamp
    tweet_timestamp = models.CharField( max_length = 255, blank = True )
    tweet_timestamp_datetime = models.DateTimeField( null = True, blank = True )
    timestamp_year = models.IntegerField( null = True, blank = True )
    timestamp_month = models.IntegerField( null = True, blank = True )
    timestamp_day = models.IntegerField( null = True, blank = True )
    timestamp_hour = models.IntegerField( null = True, blank = True )
    timestamp_minute = models.IntegerField( null = True, blank = True )
    timestamp_second = models.IntegerField( null = True, blank = True )

    # basic information
    twitter_tweet_id = models.BigIntegerField()
    tweet_text = models.TextField( null = True, blank = True )
    tweet_text_length = models.IntegerField( null = True, blank = True )

    # user information
    twitter_user = models.ForeignKey( 'Twitter_User', null = True, blank = True, related_name = 'author_user' )
    twitter_user_twitter_id = models.BigIntegerField()
    twitter_user_screenname = models.CharField( max_length = 255 )
    user_follower_count = models.IntegerField( null = True, blank = True )
    user_favorites_count = models.IntegerField( null = True, blank = True )
    user_created = models.CharField( max_length = 255, blank = True, null = True )
    user_created_datetime = models.DateTimeField( null = True, blank = True )
    user_location = models.TextField( null = True, blank=True )

    # rewteets
    tweet_retweet_count = models.IntegerField( null = True, blank = True )
    tweet_retweet_user = models.ForeignKey( 'Twitter_User', null = True, blank = True, related_name = 'retweet_user' )
    tweet_retweet_user_twitter_id = models.BigIntegerField( null = True, blank = True )
    tweet_retweet_id = models.BigIntegerField( null = True, blank = True )

    # location
    tweet_location = models.TextField( null = True, blank = True )
    tweet_has_location = models.IntegerField( null = True, blank = True )
    tweet_latitude = models.CharField( max_length = 255, blank = True, null = True )
    tweet_longitude = models.CharField( max_length = 255, blank = True, null = True )
    
    # user mentions
    tweet_user_mention_count = models.IntegerField( null = True, blank = True )
    tweet_users_mentioned = models.TextField( null = True, blank = True )
    tweet_users_mentioned_ids = models.TextField( null = True, blank = True )

    # hashtags
    tweet_hashtag_mention_count = models.IntegerField( null = True, blank = True )
    tweet_hashtags_mentioned = models.TextField( null = True, blank = True )

    # URLs
    tweet_url_count = models.IntegerField( null = True, blank = True )
    tweet_shortened_urls_mentioned = models.TextField( null = True, blank = True )
    tweet_full_urls_mentioned = models.TextField( null = True, blank = True )


    #----------------------------------------------------------------------
    # meta
    #----------------------------------------------------------------------

    # not abstract for now.
    # meta class so we know this is an abstract class.
    #class Meta:
    #    abstract = True


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
#-- END class Abstract_Tweet --#


# not abstract for now.
# class Abstract_Twitter_User( models.Model ):
class Twitter_User( models.Model ):

    twitter_user_name = models.CharField( max_length = 255, blank=True )
    twitter_user_twitter_id = models.BigIntegerField()


    #----------------------------------------------------------------------
    # meta
    #----------------------------------------------------------------------

    # not abstract for now.
    # meta class so we know this is an abstract class.
    #class Meta:
    #    abstract = True


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