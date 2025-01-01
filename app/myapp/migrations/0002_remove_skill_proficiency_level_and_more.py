# Generated by Django 5.1.4 on 2024-12-31 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='proficiency_level',
        ),
        migrations.AddField(
            model_name='skill',
            name='years_of_experience',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
