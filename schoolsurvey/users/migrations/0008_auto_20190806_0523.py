# Generated by Django 2.2.3 on 2019-08-06 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190806_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='telephone',
            field=models.CharField(max_length=255),
        ),
    ]
