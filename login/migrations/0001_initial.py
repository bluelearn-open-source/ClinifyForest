# Generated by Django 3.1.7 on 2021-04-02 10:06

from django.db import migrations, models
import login.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordUser',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('discord_tag', models.CharField(max_length=100)),
                ('avatar', models.CharField(blank=True, max_length=100, null=True)),
                ('coins', models.IntegerField(default=0)),
                ('trees', models.IntegerField(default=0)),
                ('deadtrees', models.IntegerField(default=0)),
                ('public_flags', models.IntegerField()),
                ('flags', models.IntegerField()),
                ('locale', models.CharField(max_length=100)),
                ('mfa_enabled', models.BooleanField()),
                ('room_admin', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(null=True)),
            ],
            managers=[
                ('objects', login.managers.DiscordUserOAuth2Manager()),
            ],
        ),
    ]
