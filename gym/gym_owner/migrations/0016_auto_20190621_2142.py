# Generated by Django 2.2.2 on 2019-06-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_owner', '0015_auto_20190621_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='gst_number',
            field=models.BigIntegerField(default=None),
        ),
    ]
