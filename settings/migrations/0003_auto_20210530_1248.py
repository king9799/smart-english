# Generated by Django 3.1.7 on 2021-05-30 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20210530_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='subject_name',
            field=models.CharField(max_length=255),
        ),
    ]
