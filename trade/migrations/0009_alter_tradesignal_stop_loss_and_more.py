# Generated by Django 4.2.2 on 2023-06-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0008_alter_tradesignal_entry_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradesignal',
            name='stop_loss',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tradesignal',
            name='take_profit',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True),
        ),
    ]
