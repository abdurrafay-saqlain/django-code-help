# Generated by Django 4.2.3 on 2023-07-25 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_is_client_profile_user_is_freelancer_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freelancer',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('linkedin_url', models.URLField(null=True)),
                ('facebook_url', models.URLField(null=True)),
                ('behance_url', models.URLField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
