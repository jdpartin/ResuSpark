# Generated by Django 5.1.4 on 2025-01-23 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_userinfo_github_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='additional_info',
        ),
    ]
