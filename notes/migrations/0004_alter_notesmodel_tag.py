# Generated by Django 4.0.3 on 2022-08-17 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_notesmodel_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesmodel',
            name='tag',
            field=models.CharField(blank=True, choices=[('3dcg', '3dcg'), ('web', 'web'), ('Linux', 'Linux'), ('other', 'other')], max_length=30, null=True),
        ),
    ]
