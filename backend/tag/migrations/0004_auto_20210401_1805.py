# Generated by Django 3.1.7 on 2021-04-01 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0003_tag_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('-id',)},
        ),
    ]