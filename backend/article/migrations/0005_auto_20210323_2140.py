# Generated by Django 3.1.7 on 2021-03-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0003_tag_slug'),
        ('article', '0004_auto_20210323_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tag.Tag'),
        ),
    ]
