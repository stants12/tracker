# Generated by Django 5.0.6 on 2024-05-19 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
