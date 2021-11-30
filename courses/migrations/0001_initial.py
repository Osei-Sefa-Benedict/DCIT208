# Generated by Django 3.2.9 on 2021-11-30 11:19

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
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=225)),
                ('created', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('student_rating', models.IntegerField(default=0)),
                ('language', models.CharField(max_length=225)),
                ('course_length', models.CharField(default=0, max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('free_price', models.BooleanField(default=False, verbose_name='Free Course')),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ManyToManyField(blank=True, to='courses.Comment')),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('file', models.FileField(upload_to='')),
                ('length', models.IntegerField()),
                ('description', models.CharField(max_length=30)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(blank=True, max_length=225, null=True)),
                ('section_number', models.IntegerField(blank=True, null=True)),
                ('episodes', models.ManyToManyField(blank=True, to='courses.Episode')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='course_sections',
            field=models.ManyToManyField(blank=True, to='courses.CourseSection'),
        ),
        migrations.AddField(
            model_name='courses',
            name='rating',
            field=models.ManyToManyField(blank=True, to='courses.Rate'),
        ),
    ]