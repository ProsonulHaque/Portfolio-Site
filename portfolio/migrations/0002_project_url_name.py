# Generated by Django 3.0.7 on 2020-06-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]