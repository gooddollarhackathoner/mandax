# Generated by Django 2.1.7 on 2019-03-15 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_twilio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('origin_quantity', models.DecimalField(decimal_places=8, max_digits=28)),
                ('origin_currency', models.CharField(max_length=3)),
                ('destination_quantity', models.DecimalField(decimal_places=8, max_digits=28)),
                ('destination_currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='MandexUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('ils_balance', models.DecimalField(decimal_places=8, max_digits=28)),
                ('gdd_balance', models.DecimalField(decimal_places=8, max_digits=28)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_from', models.CharField(max_length=50)),
                ('sent_to', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('quantity', models.DecimalField(decimal_places=8, max_digits=28)),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
    ]
