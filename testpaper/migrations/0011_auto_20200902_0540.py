# Generated by Django 3.1 on 2020-09-02 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpaper', '0010_useranswers_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswers',
            name='marks',
            field=models.IntegerField(blank=True),
        ),
    ]
