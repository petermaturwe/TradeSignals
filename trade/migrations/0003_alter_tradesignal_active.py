# Generated by Django 4.2.2 on 2023-06-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_tradesignal_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradesignal',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
