# Generated by Django 2.1.7 on 2019-03-24 05:08

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):
    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=markdownx.models.MarkdownxField(verbose_name='内容'),
        ),
    ]
