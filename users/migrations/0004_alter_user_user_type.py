# Generated by Django 4.2.3 on 2023-07-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('admin', 'ADMIN'), ('freelancer', 'FREELANCER'), ('client', 'CLIENT')], default='admin', max_length=250),
        ),
    ]
