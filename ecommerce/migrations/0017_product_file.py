# Generated by Django 4.2.2 on 2023-07-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0016_remove_product_image_urls_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.URLField(blank=True, null=True),
        ),
    ]
