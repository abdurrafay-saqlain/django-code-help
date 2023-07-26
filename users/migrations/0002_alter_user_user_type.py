# Generated by Django 4.2.3 on 2023-07-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('admin', 'ADMIN'), ('freelancer', 'FREELANCER'), ('client', 'CLIENT')], default='admin', max_length=250),
        ),
    ]
