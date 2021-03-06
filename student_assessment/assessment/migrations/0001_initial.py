# Generated by Django 2.2.12 on 2020-04-28 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses_code', models.CharField(max_length=30, unique=True)),
                ('courses_name', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'courses_table',
            },
        ),
        migrations.CreateModel(
            name='LecturerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecturer_nidn', models.CharField(max_length=30, unique=True)),
                ('lecturer_name', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'lecturer_table',
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_nim', models.CharField(max_length=30, unique=True)),
                ('student_name', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'students_table',
            },
        ),
    ]
