# Generated by Django 2.2.14 on 2021-04-27 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]