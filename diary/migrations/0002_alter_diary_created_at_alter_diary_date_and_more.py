# Generated by Django 4.1.4 on 2022-12-23 06:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='text',
            field=models.CharField(max_length=200, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Updated at'),
        ),
    ]
