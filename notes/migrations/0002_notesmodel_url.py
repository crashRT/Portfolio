# Generated by Django 4.0.3 on 2022-08-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notesmodel',
            name='url',
            field=models.TextField(default='#'),
            preserve_default=False,
        ),
    ]
