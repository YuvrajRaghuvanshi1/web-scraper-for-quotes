# Generated by Django 3.0.5 on 2020-04-24 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_S', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
