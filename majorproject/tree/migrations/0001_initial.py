# Generated by Django 2.0.5 on 2018-05-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=120)),
                ('othername', models.CharField(max_length=120)),
            ],
        ),
    ]