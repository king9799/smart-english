# Generated by Django 3.1.7 on 2021-05-30 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_auto_20210530_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_type', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='LessonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_types', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Lesson type',
                'verbose_name_plural': 'Lesson Types',
            },
        ),
        migrations.CreateModel(
            name='Patterns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patterns', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Lesson Pattern',
                'verbose_name_plural': 'Lesson Patterns',
            },
        ),
        migrations.AlterModelOptions(
            name='subjects',
            options={'verbose_name': 'Subject', 'verbose_name_plural': 'Subjects'},
        ),
        migrations.AlterField(
            model_name='timetable',
            name='finish_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='start_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='group_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_types', to='settings.group'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='lesson_pattern',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_patterns', to='settings.patterns'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='lesson_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='settings.lessontype'),
        ),
    ]
