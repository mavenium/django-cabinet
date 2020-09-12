# Generated by Django 2.1.4 on 2018-12-12 02:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("cabinet", "0003_file__overwrite")]

    operations = [
        migrations.AddField(
            model_name="file",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="created at",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="file",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="updated at"),
        ),
        migrations.AddField(
            model_name="folder",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="created at",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="folder",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="updated at"),
        ),
    ]
