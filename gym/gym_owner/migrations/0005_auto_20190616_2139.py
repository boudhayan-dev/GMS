# Generated by Django 2.2.2 on 2019-06-16 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_owner', '0004_auto_20190616_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment_details',
            old_name='equipment_id',
            new_name='equipment',
        ),
    ]
