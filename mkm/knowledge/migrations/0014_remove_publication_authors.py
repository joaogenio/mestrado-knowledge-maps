# Generated by Django 4.0.3 on 2022-05-08 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0013_alter_project_desc_alter_publication_abstract_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='authors',
        ),
    ]
