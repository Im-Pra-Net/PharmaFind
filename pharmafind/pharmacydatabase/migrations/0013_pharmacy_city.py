# Generated by Django 4.0.6 on 2022-07-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacydatabase', '0012_remove_pharmacy_latitude_remove_pharmacy_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
    ]
