# Generated by Django 3.1 on 2020-09-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0013_auto_20200906_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='hint_image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question_image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='sheet_name',
            name='concept_image',
            field=models.ImageField(upload_to='images'),
        ),
    ]