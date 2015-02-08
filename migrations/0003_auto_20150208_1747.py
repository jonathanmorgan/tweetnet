# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetnet', '0002_auto_20150208_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='tweet_location',
            new_name='tweet_place',
        ),
    ]
