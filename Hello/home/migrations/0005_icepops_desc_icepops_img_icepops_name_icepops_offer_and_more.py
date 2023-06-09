# Generated by Django 4.1.3 on 2022-11-08 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_icepops'),
    ]

    operations = [
        migrations.AddField(
            model_name='icepops',
            name='desc',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='icepops',
            name='img',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='icepops',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='icepops',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='icepops',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
