# Generated by Django 4.1 on 2022-08-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_follower'),
    ]

    operations = [
        migrations.AddField(
            model_name='collector',
            name='followers',
            field=models.ManyToManyField(to='main_app.follower'),
        ),
    ]
