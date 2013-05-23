'''
Copyright 2012, 2013 Jonathan Morgan

This file is part of http://github.com/jonathanmorgan/tweetnet.

tweetnet is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

tweetnet is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with http://github.com/jonathanmorgan/tweetnet. If not, see http://www.gnu.org/licenses/.
'''
from __future__ import unicode_literals

# python imports
import datetime

# django imports
from django.db import models
import django.utils.encoding
from django.utils.encoding import python_2_unicode_compatible

# Twitter variables
TWITTER_DATE_FORMAT = '%a %b %d %H:%M:%S +0000 %Y'

# not abstract for now.
@python_2_unicode_compatible
class Abstract_Twitter_User( models.Model ):


    #============================================================================
    # Constants-ish
    #============================================================================


    TWITTER_DATE_FORMAT = '%a %b %d %H:%M:%S +0000 %Y'
    

    #============================================================================
    # Django model fields.
    #============================================================================

    twitter_user_name = models.CharField( max_length = 255, blank = True, null = True ) # 'screen_name'
    twitter_user_twitter_id = models.BigIntegerField() # 'id'
    created_at = models.CharField( max_length = 255, blank = True, null = True ) # 'created_at'
    created_at_dt = models.DateTimeField( null = True, blank = True ) # 'created_at'
    description = models.TextField( null = True, blank = True ) # 'description'
    followers_count = models.IntegerField( null = True, blank = True ) # 'followers_count'
    favourites_count = models.IntegerField( null = True, blank = True ) # 'favourites_count'
    location = models.TextField( null = True, blank=True ) # 'location'
    name = models.CharField( max_length = 255, blank = True, null = True ) # 'name'
    lang = models.CharField( max_length = 255, blank = True, null = True ) # 'lang'
    image_url = models.CharField( max_length = 255, blank = True, null = True ) # 'profile_image_url'
    image_url_https = models.CharField( max_length = 255, blank = True, null = True ) # 'profile_image_url_https'
    is_protected = models.BooleanField( blank = True, default = False ) # 'protected'
    is_geo_enabled = models.BooleanField( blank = True, default = False ) # 'geo_enabled'
    is_verified = models.BooleanField( blank = True, default = False ) # 'verified'
    time_zone = models.CharField( max_length = 255, blank = True, null = True ) # 'time_zone'
    url = models.CharField( max_length = 255, blank = True, null = True ) # 'url'
    utc_offset = models.IntegerField( null = True, blank = True ) # 'utc_offset'

    '''
    Not included (yet):
    [{u'contributors_enabled': False,
      u'default_profile': False,
      u'default_profile_image': False,
      u'description': None,
      u'entities': {u'description': {u'urls': []}},
      u'favourites_count': 0,
      u'follow_request_sent': False,
      u'following': False,
      u'id_str': u'16529583',
      u'is_translator': False,
      u'listed_count': 8,
      u'notifications': False,
      u'profile_background_color': u'1A1B1F',
      u'profile_background_image_url': u'http://a0.twimg.com/images/themes/theme9/bg.gif',
      u'profile_background_image_url_https': u'https://si0.twimg.com/images/themes/theme9/bg.gif',
      u'profile_background_tile': False,
      u'profile_link_color': u'2FC2EF',
      u'profile_sidebar_border_color': u'181A1E',
      u'profile_sidebar_fill_color': u'252429',
      u'profile_text_color': u'666666',
      u'profile_use_background_image': True,
      u'status': {u'contributors': None,
       u'coordinates': None,
       u'created_at': u'Sun May 12 00:44:07 +0000 2013',
       u'entities': {u'hashtags': [],
        u'urls': [{u'display_url': u'instagram.com/p/ZMR7QLM9VU/',
          u'expanded_url': u'http://instagram.com/p/ZMR7QLM9VU/',
          u'indices': [102, 124],
          u'url': u'http://t.co/WLcG24eKpL'}],
        u'user_mentions': []},
       u'favorited': False,
       u'geo': None,
       u'id': 333382044186980353,
       u'id_str': u'333382044186980353',
       u'in_reply_to_screen_name': None,
       u'in_reply_to_status_id': None,
       u'in_reply_to_status_id_str': None,
       u'in_reply_to_user_id': None,
       u'in_reply_to_user_id_str': None,
       u'place': None,
       u'possibly_sensitive': False,
       u'retweet_count': 0,
       u'retweeted': False,
       u'source': u'<a href="http://instagram.com" rel="nofollow">Instagram</a>',
       u'text': u'...revealed as Hancock Fabrics is converted to a gym.  I want to know what he says! @ Former Hancock\u2026 http://t.co/WLcG24eKpL',
       u'truncated': False},
      u'statuses_count': 89,
    '''

    #----------------------------------------------------------------------
    # meta
    #----------------------------------------------------------------------

    # meta class so we know this is an abstract class.
    class Meta:
        abstract = True


    #----------------------------------------------------------------------
    # instance methods
    #----------------------------------------------------------------------

    def __str__( self ):
 
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

#-- END class Abstract_Twitter_User --#


@python_2_unicode_compatible
class Twitter_User( Abstract_Twitter_User ):

    #----------------------------------------------------------------------
    # instance methods
    #----------------------------------------------------------------------

    def __str__( self ):
 
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

# not abstract for now.
@python_2_unicode_compatible
class Abstract_Tweet( models.Model ):


    #============================================================================
    # Constants-ish
    #============================================================================


    TWITTER_DATE_FORMAT = '%a %b %d %H:%M:%S +0000 %Y'


    #============================================================================
    # Django model fields.
    #============================================================================

    # timestamp
    tweet_timestamp = models.CharField( max_length = 255, null = True, blank = True )
    tweet_timestamp_dt = models.DateTimeField( null = True, blank = True )
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
    tweet_language = models.CharField( max_length = 255, null = True, blank = True )

    # user information
    twitter_user = models.ForeignKey( 'Twitter_User', null = True, blank = True, related_name = 'author_user' )
    twitter_user_twitter_id = models.BigIntegerField()
    twitter_user_screenname = models.CharField( max_length = 255 )
    user_follower_count = models.IntegerField( null = True, blank = True )
    user_favorites_count = models.IntegerField( null = True, blank = True )
    user_created = models.CharField( max_length = 255, blank = True, null = True )
    user_created_dt = models.DateTimeField( null = True, blank = True )
    user_location = models.TextField( null = True, blank=True )

    # rewteets
    tweet_retweet_count = models.IntegerField( null = True, blank = True )
    tweet_retweet_user = models.ForeignKey( Twitter_User, null = True, blank = True, related_name = 'retweet_user' )
    tweet_retweet_user_twitter_id = models.BigIntegerField( null = True, blank = True )
    tweet_retweet_id = models.BigIntegerField( null = True, blank = True )

    # location
    tweet_location = models.TextField( null = True, blank = True )
    tweet_has_location = models.IntegerField( null = True, blank = True )
    tweet_coordinates = models.CharField( max_length = 255, blank = True, null = True )
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

    # meta class so we know this is an abstract class.
    class Meta:
        abstract = True


    #----------------------------------------------------------------------
    # instance methods
    #----------------------------------------------------------------------

    def __str__( self ):
 
        # return reference
        string_OUT = ''
 
        if ( self.id ):
        
            string_OUT = str( self.id ) + " - "
            
        #-- END check to see if ID --#
                
        string_OUT += str( self.twitter_tweet_id )
        
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

    #-- END method __str__() --#

#-- END class Abstract_Tweet --#


@python_2_unicode_compatible
class Tweet( Abstract_Tweet ):


    def __str__( self ):
 
        # return reference
        string_OUT = ''
 
        if ( self.id ):
        
            string_OUT = str( self.id ) + " - "
            
        #-- END check to see if ID --#
                
        string_OUT += str( self.twitter_tweet_id )
        
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

    #-- END method __str__() --#


#-- END class Tweet --#