# Generated by Django 3.2.6 on 2021-10-15 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0004_auto_20210915_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturemodel',
            name='discription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='picturemodel',
            name='picture1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picturemodel',
            name='picture2',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picturemodel',
            name='picture3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picturemodel',
            name='picture4',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picturemodel',
            name='picture5',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picturemodel',
            name='picture6',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
