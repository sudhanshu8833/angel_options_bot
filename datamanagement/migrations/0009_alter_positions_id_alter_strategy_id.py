# Generated by Django 4.0.6 on 2022-08-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamanagement', '0008_delete_orders_delete_user1_rename_lot_strategy_lots_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positions',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
