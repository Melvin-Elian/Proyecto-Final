# Generated by Django 3.0.7 on 2020-07-10 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_auto_20200709_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]
