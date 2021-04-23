# Generated by Django 3.1.7 on 2021-04-01 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0007_auto_20210324_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default='asghar', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='arts', to=settings.AUTH_USER_MODEL),
        ),
    ]