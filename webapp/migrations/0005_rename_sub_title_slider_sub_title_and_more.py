# Generated by Django 5.0 on 2023-12-23 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_rename_name_slider_sub_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='sub_title',
            new_name='Sub_title',
        ),
        migrations.RenameField(
            model_name='slider',
            old_name='title',
            new_name='Title',
        ),
    ]
