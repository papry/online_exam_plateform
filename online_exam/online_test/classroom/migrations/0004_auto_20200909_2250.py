# Generated by Django 3.1 on 2020-09-09 16:50

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20200815_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takenquiz',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now),
        ),
    ]
