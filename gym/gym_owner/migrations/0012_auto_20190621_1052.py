# Generated by Django 2.2.2 on 2019-06-21 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_owner', '0011_auto_20190621_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='pan',
            field=models.CharField(max_length=20),
        ),
    ]
