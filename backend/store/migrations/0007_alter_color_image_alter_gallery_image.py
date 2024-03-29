# Generated by Django 4.2 on 2023-10-28 21:01

from django.db import migrations, models
import userauths.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=userauths.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.FileField(default='gallery.jpg', upload_to=userauths.models.user_directory_path),
        ),
    ]
