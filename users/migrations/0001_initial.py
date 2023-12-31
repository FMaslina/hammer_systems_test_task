# Generated by Django 4.2.4 on 2023-08-18 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', models.CharField(max_length=20, unique=True, verbose_name='Номер телефона')),
                ('first_name', models.TextField(verbose_name='Имя')),
                ('last_name', models.TextField(verbose_name='Фамилия')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Юзернейм')),
                ('referral_code', models.CharField(max_length=6, unique=True, verbose_name='Реферральный код')),
                ('invite_code', models.CharField(blank=True, max_length=6, null=True, verbose_name='Код пригласившего')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
