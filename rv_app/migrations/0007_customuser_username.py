# Generated by Django 4.2 on 2023-04-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rv_app', '0006_customuser_alter_admin_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='', max_length=150, unique=True),
        ),
    ]
