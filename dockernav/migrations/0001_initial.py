# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 19:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('rand_int', models.IntegerField(default=0, unique=True)),
                ('image', models.CharField(choices=[(b'vnc', b'wallace123/docker-vnc'), (b'jabber', b'wallace123/docker-jabber')], max_length=10)),
                ('vnc_pass', models.CharField(blank=True, max_length=20)),
                ('jabber_ip', models.CharField(blank=True, max_length=20)),
                ('user1', models.CharField(blank=True, max_length=20)),
                ('pass1', models.CharField(blank=True, max_length=20)),
                ('user2', models.CharField(blank=True, max_length=20)),
                ('pass2', models.CharField(blank=True, max_length=20)),
                ('category', models.CharField(blank=True, max_length=30)),
                ('loop_file', models.CharField(blank=True, max_length=30)),
                ('dservice', models.CharField(blank=True, max_length=30)),
                ('dockerd', models.CharField(blank=True, max_length=30)),
                ('device', models.CharField(blank=True, max_length=30)),
                ('port', models.CharField(blank=True, max_length=6)),
                ('docker_run', models.CharField(blank=True, max_length=30)),
                ('docker_lib', models.CharField(blank=True, max_length=30)),
                ('docker_bridge', models.CharField(blank=True, max_length=16)),
                ('mount_point', models.CharField(blank=True, max_length=30)),
                ('container', models.CharField(blank=True, max_length=30)),
                ('dservice_path', models.CharField(blank=True, max_length=40)),
                ('docker', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='NavServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('host', models.CharField(max_length=20)),
                ('port', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='container',
            name='navserver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dockernav.NavServer'),
        ),
        migrations.AddField(
            model_name='container',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
