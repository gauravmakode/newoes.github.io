# Generated by Django 3.1 on 2020-09-05 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sheet', '0011_auto_20200905_0703'),
        ('user', '0003_auto_20200905_0425'),
    ]

    operations = [
        migrations.CreateModel(
            name='userlevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('select_level', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sheet.level')),
                ('select_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='level',
        ),
    ]
