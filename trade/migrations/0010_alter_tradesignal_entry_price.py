# Generated by Django 4.2.2 on 2023-06-29 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0009_alter_tradesignal_stop_loss_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradesignal',
            name='entry_price',
            field=models.DecimalField(decimal_places=10, default=None, max_digits=20, null=True),
        ),
    ]
