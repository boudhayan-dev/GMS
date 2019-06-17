# Generated by Django 2.2.2 on 2019-06-16 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gym_owner', '0006_auto_20190616_2149'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('is_delete', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('changed_date', models.DateTimeField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contact', models.BigIntegerField()),
                ('aadhar', models.BigIntegerField()),
                ('pan', models.CharField(max_length=20)),
                ('dob', models.DateTimeField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default=None, max_length=10, null=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='static/images/gym_customer/profile')),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gym_owner.Address')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_owner.Gym')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Owner',
            },
        ),
    ]