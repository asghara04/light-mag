# Generated by Django 3.1.5 on 2021-01-21 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=35)),
                ('join_date', models.DateField(auto_now_add=True)),
                ('last_login', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('pubmail', models.EmailField(blank=True, max_length=30, null=True, unique=True)),
                ('bio', models.TextField(blank=True, max_length=400, null=True)),
                ('about', models.TextField(blank=True, max_length=400, null=True)),
                ('instagram_link', models.URLField(blank=True, max_length=35, null=True)),
                ('facebook_link', models.URLField(blank=True, max_length=35, null=True)),
                ('github_link', models.URLField(blank=True, max_length=35, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('favorite_cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category')),
                ('prof_picture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='image.image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
