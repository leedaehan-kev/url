# Generated by Django 3.2.3 on 2021-07-01 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='calendar_type',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='color',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='font',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='language',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='stamp',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='type',
        ),
    ]