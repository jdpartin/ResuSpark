# Generated by Django 5.1.4 on 2025-01-19 02:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_resume_resumeproject_resume_projects_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
