# Generated by Django 4.0.1 on 2022-03-10 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0029_brand_product_product_off_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
