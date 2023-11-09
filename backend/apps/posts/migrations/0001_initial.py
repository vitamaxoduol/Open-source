# Generated by Django 4.2.6 on 2023-11-09 22:37

from django.db import migrations, models
import django.utils.timezone
import django_resized.forms
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, default=0, max_length=112, null=True)),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[250, 200], upload_to='images')),
                ('video', models.FileField(blank=True, default=0, null=True, upload_to='videos/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
