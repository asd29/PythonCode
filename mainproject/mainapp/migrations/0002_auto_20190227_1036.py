# Generated by Django 2.1.7 on 2019-02-27 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_contact_number',
            new_name='contact_number',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_last_name',
            new_name='last_name',
        ),
    ]
