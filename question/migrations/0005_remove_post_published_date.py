# Generated by Django 2.1.5 on 2019-01-19 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20190118_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
    ]
