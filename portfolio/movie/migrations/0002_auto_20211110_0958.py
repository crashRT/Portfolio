# Generated by Django 3.2.6 on 2021-11-10 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='thumbnail',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='picture1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
