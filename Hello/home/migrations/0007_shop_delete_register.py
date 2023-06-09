# Generated by Django 4.1.3 on 2022-11-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('card', models.CharField(max_length=122)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
