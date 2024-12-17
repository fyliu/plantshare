# Generated by Django 5.0.9 on 2024-12-07 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_category_options_alter_commodity_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='want',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]