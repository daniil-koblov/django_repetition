# Generated by Django 5.1.3 on 2024-11-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminarapp_4_1', '0002_alter_author_bio_alter_author_birthday'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='birthday',
            field=models.DateField(),
        ),
    ]
