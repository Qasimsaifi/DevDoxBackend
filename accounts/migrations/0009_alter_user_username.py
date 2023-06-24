# Generated by Django 4.2.2 on 2023-06-24 20:35

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_user_user_name_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=accounts.models.generate_unique_username, max_length=240, unique=True),
        ),
    ]
