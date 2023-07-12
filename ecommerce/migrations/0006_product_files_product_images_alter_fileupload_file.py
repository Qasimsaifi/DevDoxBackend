# Generated by Django 4.2.2 on 2023-07-12 11:13

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_remove_product_files_remove_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='files',
            field=models.ManyToManyField(related_name='products', to='ecommerce.fileupload'),
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(related_name='products', to='ecommerce.productimage'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='file'),
        ),
    ]
