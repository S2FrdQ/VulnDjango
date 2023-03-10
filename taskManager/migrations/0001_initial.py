# Generated by Django 3.2.18 on 2023-03-04 14:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Default', max_length=50)),
                ('text', models.CharField(max_length=500)),
                ('start_date', models.DateTimeField(verbose_name='date started')),
                ('due_date', models.DateTimeField(default=datetime.datetime(2023, 3, 11, 14, 55, 6, 69151, tzinfo=utc), verbose_name='date due')),
                ('priority', models.IntegerField(default=1)),
                ('users_assigned', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(default='', max_length=3000)),
                ('reset_token', models.CharField(default='', max_length=7)),
                ('reset_token_expiration', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('title', models.CharField(default='N/A', max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='date created')),
                ('due_date', models.DateTimeField(default=datetime.datetime(2023, 3, 11, 14, 55, 6, 70100, tzinfo=utc), verbose_name='date due')),
                ('completed', models.NullBooleanField(default=False)),
                ('project', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='taskManager.project')),
                ('users_assigned', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='N/A', max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('user', models.CharField(default='ancestor', max_length=200)),
                ('task', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='taskManager.task')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300)),
                ('path', models.CharField(default='', max_length=3000)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taskManager.project')),
            ],
        ),
    ]
