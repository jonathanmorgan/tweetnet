# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Tweets( models.Model ):

    tweet_timestamp = models.CharField( max_length = 255, blank = True )
    tweet_timestamp_datetime = models.DateTimeField( null = True, blank = True )
    twitter_tweet_id = models.BigIntegerField()
    twitter_user_id = models.IntegerField( null = True, blank = True )
    twitter_user_screenname = models.CharField( max_length = 255, primary_key = True )
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

#-- END class NewsTweets --#