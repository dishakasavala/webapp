# Generated by Django 5.0 on 2023-12-26 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_remove_slider_u_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='maincatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(default='', upload_to='media/')),
            ],
        ),
    ]
