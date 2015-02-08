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
    timestamp_ms = models.CharField( max_length = 255, null = True, blank = True )

    # basic information
    twitter_tweet_id = models.BigIntegerField()
    tweet_text = models.TextField( null = True, blank = True )
    tweet_text_length = models.IntegerField( null = True, blank = True )
    tweet_language = models.CharField( max_length = 255, null = True, blank = True )

    # user information
    twitter_user = models.ForeignKey( 'Twitter_User', null = True, blank = True, related_name = 'author_user' )
    twitter_user_twitter_id = models.BigIntegerField()
    twitter_user_screenname = models.CharField( max_length = 255 )
    user_followers_count = models.IntegerField( null = True, blank = True )
    user_favorites_count = models.IntegerField( null = True, blank = True )
    user_friends_count = models.IntegerField( null = True, blank = True )
    user_created = models.CharField( max_length = 255, blank = True, null = True )
    user_created_dt = models.DateTimeField( null = True, blank = True )
    user_location = models.TextField( null = True, blank=True )
    user_description = models.TextField( null = True, blank=True )
    user_statuses_count = models.IntegerField( null = True, blank = True )

    # replies
    tweet_in_reply_to_screen_name = models.CharField( max_length = 255, null = True, blank = True )
    tweet_in_reply_to_status_id = models.BigIntegerField( null = True, blank=True )
    tweet_in_reply_to_status_id_str = models.CharField( max_length = 255, null = True, blank = True )
    tweet_in_reply_to_user_id = models.BigIntegerField( null = True, blank=True )
    tweet_in_reply_to_user_id_str = models.CharField( max_length = 255, null = True, blank = True )

    # rewteets
    tweet_retweet_count = models.IntegerField( null = True, blank = True )
    tweet_retweet_user = models.ForeignKey( Twitter_User, null = True, blank = True, related_name = 'retweet_user' )
    tweet_retweet_user_twitter_id = models.BigIntegerField( null = True, blank = True )
    tweet_retweet_id = models.BigIntegerField( null = True, blank = True )

    # location
    tweet_geo = models.CharField( max_length = 255, blank = True, null = True )
    tweet_place = models.TextField( null = True, blank = True )
    tweet_has_location = models.IntegerField( null = True, blank = True )
    tweet_coordinates = models.CharField( max_length = 255, blank = True, null = True )
    tweet_latitude = models.CharField( max_length = 255, blank = True, null = True )
    tweet_longitude = models.CharField( max_length = 255, blank = True, null = True )
    
    # user mentions
    tweet_user_mention_count = models.IntegerField( null = True, blank = True )
    tweet_users_mentioned_ids = models.TextField( null = True, blank = True )
    tweet_users_mentioned_screennames = models.TextField( null = True, blank = True )

    # hashtags
    tweet_hashtag_mention_count = models.IntegerField( null = True, blank = True )
    tweet_hashtags_mentioned = models.TextField( null = True, blank = True )

    # URLs
    tweet_url_count = models.IntegerField( null = True, blank = True )
    tweet_shortened_urls_mentioned = models.TextField( null = True, blank = True )
    tweet_display_urls_mentioned = models.TextField( null = True, blank = True )
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


@python_2_unicode_compatible
class Tweet_JSON( models.Model ):

    # fields
    tweet = models.ForeignKey( 'Tweet' )
    tweet_json = models.TextField()
    

    def __str__( self ):
 
        # return reference
        string_OUT = ''
 
        if ( self.id ):
        
            string_OUT = str( self.id ) + " - "
            
        #-- END check to see if ID --#
                
        # got a related tweet?
        if  ( self.tweet ):
        
            string_OUT += "JSON for " + str( self.twitter_tweet_id )
            
        #-- END check to see if tweet. --#
 
        return string_OUT

    #-- END method __str__() --#


#-- END class Tweet_JSON --#