# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tweet'
        db.create_table(u'tweetnet_tweet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tweet_timestamp', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tweet_timestamp_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('timestamp_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('timestamp_month', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('timestamp_day', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('timestamp_hour', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('timestamp_minute', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('timestamp_second', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('twitter_tweet_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('tweet_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tweet_text_length', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tweet_language', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('twitter_user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='author_user', null=True, to=orm['tweetnet.Twitter_User'])),
            ('twitter_user_twitter_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('twitter_user_screenname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user_follower_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('user_favorites_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('user_created_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('user_location', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tweet_retweet_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tweet_retweet_user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='retweet_user', null=True, to=orm['tweetnet.Twitter_User'])),
            ('tweet_retweet_user_twitter_id', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('tweet_retweet_id', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('tweet_location', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tweet_has_location', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tweet_coordinates', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tweet_latitude', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tweet_longitude', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tweet_user_mention_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tweet_users_mentioned', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tweet_users_mentioned_ids', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tweet_hashtag_mention_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tweet_hashtags_mentioned', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tweet_url_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tweet_shortened_urls_mentioned', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tweet_full_urls_mentioned', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'tweetnet', ['Tweet'])

        # Adding model 'Twitter_User'
        db.create_table(u'tweetnet_twitter_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('twitter_user_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('twitter_user_twitter_id', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'tweetnet', ['Twitter_User'])


    def backwards(self, orm):
        # Deleting model 'Tweet'
        db.delete_table(u'tweetnet_tweet')

        # Deleting model 'Twitter_User'
        db.delete_table(u'tweetnet_twitter_user')


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
            'tweet_retweet_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'retweet_user'", 'null': 'True', 'to': u"orm['tweetnet.Twitter_User']"}),
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
            'twitter_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'author_user'", 'null': 'True', 'to': u"orm['tweetnet.Twitter_User']"}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'twitter_user_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_user_twitter_id': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['tweetnet']