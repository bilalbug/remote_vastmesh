# Generated by Django 4.1 on 2023-05-03 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rv_app', '0011_remove_customuser_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='skill_list',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='required_skills',
        ),
    ]