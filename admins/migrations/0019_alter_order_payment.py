# Generated by Django 4.0.1 on 2022-03-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0018_order_buy_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('COD', 'COD'), ('PayPal', 'PayPal'), ('RazorPay', 'RazorPay')], max_length=200, null=True),
        ),
    ]
