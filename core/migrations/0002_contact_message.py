# Generated by Django 3.2.7 on 2021-09-24 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
