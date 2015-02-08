# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet_timestamp', models.CharField(max_length=255, null=True, blank=True)),
                ('tweet_timestamp_dt', models.DateTimeField(null=True, blank=True)),
                ('timestamp_year', models.IntegerField(null=True, blank=True)),
                ('timestamp_month', models.IntegerField(null=True, blank=True)),
                ('timestamp_day', models.IntegerField(null=True, blank=True)),
                ('timestamp_hour', models.IntegerField(null=True, blank=True)),
                ('timestamp_minute', models.IntegerField(null=True, blank=True)),
                ('timestamp_second', models.IntegerField(null=True, blank=True)),
                ('twitter_tweet_id', models.BigIntegerField()),
                ('tweet_text', models.TextField(null=True, blank=True)),
                ('tweet_text_length', models.IntegerField(null=True, blank=True)),
                ('tweet_language', models.CharField(max_length=255, null=True, blank=True)),
                ('twitter_user_twitter_id', models.BigIntegerField()),
                ('twitter_user_screenname', models.CharField(max_length=255)),
                ('user_follower_count', models.IntegerField(null=True, blank=True)),
                ('user_favorites_count', models.IntegerField(null=True, blank=True)),
                ('user_created', models.CharField(max_length=255, null=True, blank=True)),
                ('user_created_dt', models.DateTimeField(null=True, blank=True)),
                ('user_location', models.TextField(null=True, blank=True)),
                ('tweet_retweet_count', models.IntegerField(null=True, blank=True)),
                ('tweet_retweet_user_twitter_id', models.BigIntegerField(null=True, blank=True)),
                ('tweet_retweet_id', models.BigIntegerField(null=True, blank=True)),
                ('tweet_location', models.TextField(null=True, blank=True)),
                ('tweet_has_location', models.IntegerField(null=True, blank=True)),
                ('tweet_coordinates', models.CharField(max_length=255, null=True, blank=True)),
                ('tweet_latitude', models.CharField(max_length=255, null=True, blank=True)),
                ('tweet_longitude', models.CharField(max_length=255, null=True, blank=True)),
                ('tweet_user_mention_count', models.IntegerField(null=True, blank=True)),
                ('tweet_users_mentioned', models.TextField(null=True, blank=True)),
                ('tweet_users_mentioned_ids', models.TextField(null=True, blank=True)),
                ('tweet_hashtag_mention_count', models.IntegerField(null=True, blank=True)),
                ('tweet_hashtags_mentioned', models.TextField(null=True, blank=True)),
                ('tweet_url_count', models.IntegerField(null=True, blank=True)),
                ('tweet_shortened_urls_mentioned', models.TextField(null=True, blank=True)),
                ('tweet_full_urls_mentioned', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Twitter_User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twitter_user_name', models.CharField(max_length=255, null=True, blank=True)),
                ('twitter_user_twitter_id', models.BigIntegerField()),
                ('created_at', models.CharField(max_length=255, null=True, blank=True)),
                ('created_at_dt', models.DateTimeField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('followers_count', models.IntegerField(null=True, blank=True)),
                ('favourites_count', models.IntegerField(null=True, blank=True)),
                ('location', models.TextField(null=True, blank=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('lang', models.CharField(max_length=255, null=True, blank=True)),
                ('image_url', models.CharField(max_length=255, null=True, blank=True)),
                ('image_url_https', models.CharField(max_length=255, null=True, blank=True)),
                ('is_protected', models.BooleanField(default=False)),
                ('is_geo_enabled', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('time_zone', models.CharField(max_length=255, null=True, blank=True)),
                ('url', models.CharField(max_length=255, null=True, blank=True)),
                ('utc_offset', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_retweet_user',
            field=models.ForeignKey(related_name='retweet_user', blank=True, to='tweetnet.Twitter_User', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tweet',
            name='twitter_user',
            field=models.ForeignKey(related_name='author_user', blank=True, to='tweetnet.Twitter_User', null=True),
            preserve_default=True,
        ),
    ]
