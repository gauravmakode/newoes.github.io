# Generated by Django 3.1 on 2020-08-21 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='sheet_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_name', models.CharField(max_length=50, unique=True)),
                ('level', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('sheet_type', models.CharField(choices=[('main', 'main'), ('practice', 'practice')], max_length=20)),
                ('no_of_questions', models.PositiveSmallIntegerField()),
                ('concept', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('concept_video', models.URLField(blank=True)),
                ('description', models.CharField(blank=True, max_length=70)),
                ('published', models.BooleanField(default=False)),
                ('select_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheet.level')),
                ('select_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheet.subject')),
                ('select_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheet.topic')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_name', models.CharField(max_length=50)),
                ('question_no', models.PositiveSmallIntegerField(null=True)),
                ('question', models.CharField(max_length=500)),
                ('questionimage', models.ImageField(blank=True, upload_to='')),
                ('blank_type', models.BooleanField(default=False)),
                ('option_a', models.CharField(blank=True, max_length=100)),
                ('option_b', models.CharField(blank=True, max_length=100)),
                ('option_c', models.CharField(blank=True, max_length=100)),
                ('option_d', models.CharField(blank=True, max_length=100)),
                ('correct_option', models.CharField(blank=True, choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')], max_length=15)),
                ('option_blank', models.CharField(blank=True, max_length=100, null=True)),
                ('hint', models.CharField(blank=True, max_length=500)),
                ('hintimage', models.ImageField(blank=True, upload_to='')),
                ('hint_video', models.URLField(blank=True)),
                ('select_sheet_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheet.sheet_name')),
            ],
            options={
                'ordering': ['question_no'],
            },
        ),
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='index', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]