# Generated by Django 5.1.3 on 2024-11-22 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField()),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(max_length=100)),
                ('views', models.PositiveIntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminarapp_4_1.author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminarapp_4_1.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminarapp_4_1.author')),
            ],
        ),
    ]
