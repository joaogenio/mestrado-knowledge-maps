# Generated by Django 4.0.3 on 2022-05-06 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0007_alter_publication_scopus_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='synced_ciencia',
            field=models.BooleanField(default=False),
        ),
    ]
