# Generated by Django 4.0.3 on 2022-06-12 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0018_alter_author_options_publication_from_ciencia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='possible_duplicates',
            field=models.ManyToManyField(to='knowledge.publication'),
        ),
    ]
