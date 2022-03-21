# Generated by Django 4.0.1 on 2022-03-16 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0033_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.CharField(max_length=200, null=True)),
                ('proceed', models.BooleanField(default=False, null=True)),
                ('remaining', models.IntegerField()),
            ],
        ),
    ]
