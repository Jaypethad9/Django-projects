# Generated by Django 4.1.3 on 2022-11-20 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_shop_delete_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='card',
            new_name='paymentMethod',
        ),
    ]
