# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetnet', '0005_auto_20150208_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hashtag_value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tweet_Download_Raw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet_timestamp', models.CharField(max_length=255, null=True, blank=True)),
                ('twitter_tweet_id', models.BigIntegerField()),
                ('tweet_text', models.TextField(null=True, blank=True)),
                ('tweet_language', models.CharField(max_length=255, null=True, blank=True)),
                ('tweet_retweet_count', models.IntegerField(null=True, blank=True)),
                ('tweet_place', models.TextField(null=True, blank=True)),
                ('tweet_user_mention_count', models.IntegerField(null=True, blank=True)),
                ('tweet_users_mentioned_screennames', models.TextField(null=True, blank=True)),
                ('tweet_users_mentioned_ids', models.TextField(null=True, blank=True)),
                ('tweet_hashtag_mention_count', models.IntegerField(null=True, blank=True)),
                ('tweet_hashtags_mentioned', models.TextField(null=True, blank=True)),
                ('tweet_url_count', models.IntegerField(null=True, blank=True)),
                ('tweet_shortened_urls_mentioned', models.TextField(null=True, blank=True)),
                ('tweet_full_urls_mentioned', models.TextField(null=True, blank=True)),
                ('tweet_display_urls_mentioned', models.TextField(null=True, blank=True)),
                ('timestamp_ms', models.CharField(max_length=255, null=True, blank=True)),
                ('tweet_geo', models.CharField(max_length=255, null=True, blank=True)),
                ('twitter_user_twitter_id', models.BigIntegerField()),
                ('twitter_user_screenname', models.CharField(max_length=255)),
                ('user_followers_count', models.IntegerField(null=True, blank=True)),
                ('user_favorites_count', models.IntegerField(null=True, blank=True)),
                ('user_friends_count', models.IntegerField(null=True, blank=True)),
                ('user_created', models.CharField(max_length=255, null=True, blank=True)),
                ('user_location', models.TextField(null=True, blank=True)),
                ('user_description', models.TextField(null=True, blank=True)),
                ('user_statuses_count', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet_Hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hashtag', models.ForeignKey(to='tweetnet.Hashtag')),
                ('tweet', models.ForeignKey(to='tweetnet.Tweet')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet_Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet', models.ForeignKey(to='tweetnet.Tweet')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet_User_Mention',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_url', models.TextField()),
                ('shortened_url', models.TextField(null=True, blank=True)),
                ('display_url', models.TextField(null=True, blank=True)),
                ('url_after_redirects', models.TextField(null=True, blank=True)),
                ('canonical_domain', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='twitter_user',
            name='statuses_count',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tweet_user_mention',
            name='mentioned_user',
            field=models.ForeignKey(to='tweetnet.Twitter_User'),
        ),
        migrations.AddField(
            model_name='tweet_user_mention',
            name='tweet',
            field=models.ForeignKey(to='tweetnet.Tweet'),
        ),
        migrations.AddField(
            model_name='tweet_url',
            name='url',
            field=models.ForeignKey(to='tweetnet.Url'),
        ),
    ]
