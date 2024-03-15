# Generated by Django 4.2.11 on 2024-03-15 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0006_bankaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('A', 'Author'), ('E', 'Editor')], max_length=1)),
            ],
        ),
    ]
