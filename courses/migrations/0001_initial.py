# Generated by Django 4.1.4 on 2023-01-27 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created', models.TimeField(auto_now_add=True)),
                ('updated', models.TimeField(auto_now=True)),
                ('content_type', models.ForeignKey(default='course', null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(blank=True, max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(blank=True, max_length=100)),
                ('video_link', models.URLField(blank=True, max_length=500)),
                ('description', models.TextField()),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.unit')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.publisher'),
        ),
        migrations.AddField(
            model_name='course',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.topic'),
        ),
    ]