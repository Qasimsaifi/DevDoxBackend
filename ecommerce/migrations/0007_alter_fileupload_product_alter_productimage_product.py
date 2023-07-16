# Generated by Django 4.2.2 on 2023-07-12 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_product_files_product_images_alter_fileupload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product'),
        ),
    ]