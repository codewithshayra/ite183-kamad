# Generated by Django 5.0 on 2024-12-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
