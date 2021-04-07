# Generated by Django 3.1.7 on 2021-04-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_discorduser_gonna_plant_tree_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discorduser',
            old_name='gonna_plant_tree',
            new_name='room_access',
        ),
        migrations.RemoveField(
            model_name='discorduser',
            name='gonna_plant_tree_on',
        ),
        migrations.AlterField(
            model_name='discorduser',
            name='room_admin',
            field=models.BooleanField(default=False),
        ),
    ]