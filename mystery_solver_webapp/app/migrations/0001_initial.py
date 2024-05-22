# Generated by Django 5.0.6 on 2024-05-17 16:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_of_the_murder', ckeditor.fields.RichTextField(max_length=700)),
                ('whereabouts', ckeditor.fields.RichTextField(max_length=1000)),
                ('evidence', ckeditor.fields.RichTextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Mystery Stories',
            },
        ),
    ]