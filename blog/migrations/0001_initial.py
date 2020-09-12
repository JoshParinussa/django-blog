# Generated by Django 3.0.6 on 2020-09-11 16:12

import blog.helpers.file
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='title')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='title')),
                ('content', models.TextField(blank=True, null=True, verbose_name='content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=blog.helpers.file.DateUploadPath('blog/blog'), verbose_name='image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog.Category', verbose_name='category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
