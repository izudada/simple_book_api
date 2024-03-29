# Generated by Django 5.0.3 on 2024-03-08 23:00

import helpers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_created_at_alter_user_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default=helpers.models.generate_id, editable=False, max_length=60, primary_key=True, serialize=False),
        ),
    ]
