# Generated by Django 2.1.7 on 2019-02-26 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_first_name', models.CharField(max_length=50)),
                ('client_last_name', models.CharField(max_length=50)),
                ('client_contact_number', models.CharField(max_length=10)),
            ],
        ),
    ]
