# Generated by Django 3.0 on 2020-01-10 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.RemoveField(
            model_name='payment',
            name='timestamp',
        ),
    ]
