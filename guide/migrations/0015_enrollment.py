# Generated by Django 4.2.11 on 2024-03-16 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0014_team_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('course_name', models.CharField(max_length=200)),
                ('enrollment_date', models.DateField()),
            ],
            options={
                'unique_together': {('student_name', 'course_name')},
            },
        ),
    ]