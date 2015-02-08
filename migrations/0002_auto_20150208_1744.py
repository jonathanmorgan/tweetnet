# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetnet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet_JSON',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet_json', models.TextField()),
                ('tweet', models.ForeignKey(to='tweetnet.Tweet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tweet',
            name='timestamp_ms',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_geo',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_in_reply_to_screen_name',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_in_reply_to_status_id',
            field=models.BigIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_in_reply_to_status_id_str',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_in_reply_to_user_id',
            field=models.BigIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_in_reply_to_user_id_str',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
