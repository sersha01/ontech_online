# Generated by Django 4.0.1 on 2022-03-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ref_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
