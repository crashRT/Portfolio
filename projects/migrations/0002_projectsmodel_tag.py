# Generated by Django 4.0.3 on 2022-08-16 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsmodel',
            name='tag',
            field=models.CharField(blank=True, choices=[('aescript', 'aescript'), ('web', 'web'), ('other', 'other')], max_length=30, null=True),
        ),
    ]
