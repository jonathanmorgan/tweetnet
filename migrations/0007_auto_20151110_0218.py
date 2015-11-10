# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetnet', '0006_auto_20150923_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet_json',
            name='twitter_tweet_id',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tweet_json',
            name='tweet',
            field=models.ForeignKey(blank=True, to='tweetnet.Tweet', null=True),
        ),
    ]
