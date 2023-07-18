# Generated by Django 4.2.1 on 2023-07-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IvatMaslov', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='famous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Person', models.CharField(max_length=100)),
                ('squad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opred', models.CharField(max_length=300)),
                ('history', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='rap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('borncounrty', models.CharField(max_length=200)),
            ],
        ),
    ]