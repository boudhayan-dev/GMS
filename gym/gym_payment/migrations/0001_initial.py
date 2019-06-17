# Generated by Django 2.2.2 on 2019-06-16 17:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gym_customer', '0004_auto_20190616_2259'),
        ('gym_owner', '0006_auto_20190616_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('is_delete', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('changed_date', models.DateTimeField(blank=True, null=True)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_customer.Customer')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_owner.Gym')),
            ],
            options={
                'verbose_name_plural': 'Payment',
            },
        ),
    ]