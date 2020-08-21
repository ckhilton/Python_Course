# Generated by Django 3.1 on 2020-08-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, default='', max_length=60)),
                ('CourseNumber', models.IntegerField(blank=True, default='')),
                ('Instructor', models.CharField(blank=True, default='', max_length=60)),
                ('Duration', models.FloatField(blank=True, default=0.0)),
            ],
        ),
    ]
