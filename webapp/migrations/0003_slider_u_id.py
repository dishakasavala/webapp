# Generated by Django 5.0 on 2023-12-23 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='u_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
