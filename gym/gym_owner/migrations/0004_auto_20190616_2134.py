# Generated by Django 2.2.2 on 2019-06-16 16:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gym_owner', '0003_auto_20190616_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_MT',
            fields=[
                ('is_delete', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('changed_date', models.DateTimeField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='owner',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/gym_owner/profile'),
        ),
        migrations.CreateModel(
            name='Equipment_Details',
            fields=[
                ('is_delete', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('changed_date', models.DateTimeField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(default=0)),
                ('equipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_owner.Equipmet_MT')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_owner.Gym')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('is_delete', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('changed_date', models.DateTimeField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('shift', models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('pre-workout', 'Pre-workout'), ('post-workout', 'Post-workout')], default=None, max_length=20, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_owner.Category_MT')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_owner.Gym')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
