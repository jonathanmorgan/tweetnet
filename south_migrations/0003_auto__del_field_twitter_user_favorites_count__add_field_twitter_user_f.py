# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Twitter_User.favorites_count'
        db.delete_column(u'tweetnet_twitter_user', 'favorites_count')

        # Adding field 'Twitter_User.favourites_count'
        db.add_column(u'tweetnet_twitter_user', 'favourites_count',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Twitter_User.favorites_count'
        db.add_column(u'tweetnet_twitter_user', 'favorites_count',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Twitter_User.favourites_count'
        db.delete_column(u'tweetnet_twitter_user', 'favourites_count')


    models = {
        u'tweetnet.tweet': {
            'Meta': {'object_name': 'Tweet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp_hour': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp_minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp_month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp_second': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_coordinates': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tweet_full_urls_mentioned': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_has_location': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_hashtag_mention_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_hashtags_mentioned': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tweet_latitude': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tweet_location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_longitude': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tweet_retweet_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_retweet_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_retweet_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'retweet_user'", 'null': 'True', 'to': u"orm['tweetnet.Twitter_User']"}),
            'tweet_retweet_user_twitter_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_shortened_urls_mentioned': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_text_length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_timestamp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tweet_timestamp_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_url_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_user_mention_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_users_mentioned': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_users_mentioned_ids': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'twitter_tweet_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'twitter_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'author_user'", 'null': 'True', 'to': u"orm['tweetnet.Twitter_User']"}),
            'twitter_user_screenname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter_user_twitter_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user_created_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user_favorites_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user_follower_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user_location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'tweetnet.twitter_user': {
            'Meta': {'object_name': 'Twitter_User'},
            'created_at': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_at_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'favourites_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'followers_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image_url_https': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_geo_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_zone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'twitter_user_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'twitter_user_twitter_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'utc_offset': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tweetnet']