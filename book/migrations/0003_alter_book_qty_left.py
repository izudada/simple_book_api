# Generated by Django 5.0.3 on 2024-03-08 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_id_alter_book_qty_left'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='qty_left',
            field=models.IntegerField(default=0),
        ),
    ]
