# Generated by Django 4.2.3 on 2023-09-08 11:28

import category.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='uploads/default.png', upload_to=category.models.get_User_file_path),
        ),
    ]
