# Generated by Django 3.1 on 2020-08-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpaper', '0007_auto_20200830_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='correct_option',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question_no',
            field=models.CharField(max_length=50),
        ),
    ]
