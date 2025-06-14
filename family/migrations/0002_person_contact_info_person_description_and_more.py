# Generated by Django 5.2 on 2025-06-11 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='contact_info',
            field=models.CharField(blank=True, help_text='Телефон, e-mail или ссылки на соцсети', max_length=255, verbose_name='Контакты'),
        ),
        migrations.AddField(
            model_name='person',
            name='description',
            field=models.TextField(blank=True, help_text='Любые заметки, истории, даты событий', verbose_name='Описание / биография'),
        ),
        migrations.AddField(
            model_name='person',
            name='is_alive',
            field=models.BooleanField(default=True, help_text='Снимите галочку, если человек скончался', verbose_name='Живой?'),
        ),
    ]
