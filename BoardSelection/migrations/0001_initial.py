# Generated by Django 4.2.1 on 2023-05-31 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_name', models.CharField(max_length=40)),
                ('subject_name', models.CharField(max_length=40)),
                ('class_name', models.CharField(max_length=25)),
                ('chapter_name', models.CharField(max_length=40)),
                ('topic_name', models.CharField(max_length=40)),
            ],
        ),
    ]
