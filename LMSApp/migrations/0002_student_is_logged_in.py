# Generated by Django 4.1.4 on 2023-01-24 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMSApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_logged_in',
            field=models.CharField(default='No', max_length=40),
        ),
    ]
