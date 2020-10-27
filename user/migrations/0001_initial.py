# Generated by Django 3.1 on 2020-09-04 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, unique=True)),
                ('basic', models.BooleanField(default=False)),
                ('foundation', models.BooleanField(default=False)),
                ('advanced', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
