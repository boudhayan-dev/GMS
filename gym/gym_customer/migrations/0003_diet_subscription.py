# Generated by Django 2.2.2 on 2019-06-16 17:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gym_owner', '0006_auto_20190616_2149'),
        ('gym_customer', '0002_auto_20190616_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet_Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('changed_date', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_customer.Customer')),
                ('diet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_owner.Diet')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
