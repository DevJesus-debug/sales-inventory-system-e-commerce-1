# Generated by Django 3.2.7 on 2021-10-14 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0016_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='default.png', upload_to='product image/'),
        ),
    ]
