# Generated by Django 4.0.4 on 2022-10-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='firstname',
        ),
        migrations.AlterField(
            model_name='newuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
