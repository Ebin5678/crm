# Generated by Django 4.2.6 on 2023-10-31 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
