# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetnet', '0003_auto_20150208_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='user_follower_count',
            new_name='user_followers_count',
        ),
        migrations.AddField(
            model_name='tweet',
            name='user_description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tweet',
            name='user_friends_count',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tweet',
            name='user_statuses_count',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
