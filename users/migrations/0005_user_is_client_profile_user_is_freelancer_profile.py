# Generated by Django 4.2.3 on 2023-07-25 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_client_profile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_freelancer_profile',
            field=models.BooleanField(default=False),
        ),
    ]
