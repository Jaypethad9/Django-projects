# Generated by Django 4.1.3 on 2022-12-09 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0004_alter_showroom_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='desc',
            new_name='desc_us',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='name',
            new_name='name_us',
        ),
    ]
