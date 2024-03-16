# Generated by Django 4.2.11 on 2024-03-16 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0012_alter_pythonmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pythonmodel',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['-created_at'], 'verbose_name_plural': 'Python'},
        ),
        migrations.AlterModelTableComment(
            name='pythonmodel',
            table_comment='student data records',
        ),
    ]