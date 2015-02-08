# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetnet', '0004_auto_20150208_1811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='tweet_users_mentioned',
            new_name='tweet_users_mentioned_screennames',
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_display_urls_mentioned',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
