# Generated by Django 3.2.9 on 2021-11-18 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_statistics', '0002_rename_statistic_statisticmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statisticmodel',
            name='clicks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='statisticmodel',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='statisticmodel',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]