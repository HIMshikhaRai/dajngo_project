# Generated by Django 2.1.7 on 2019-05-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandlordForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=160, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=160, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=160, verbose_name='Email')),
                ('password', models.CharField(max_length=160, verbose_name='Password')),
                ('re_password', models.CharField(max_length=160, verbose_name='Re- Password')),
                ('gender', models.CharField(max_length=160, verbose_name='gender')),
            ],
        ),
    ]
