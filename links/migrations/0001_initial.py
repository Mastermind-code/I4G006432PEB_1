# Generated by Django 4.0.5 on 2022-07-31 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_url', models.URLField()),
                ('description', models.CharField(max_length=200)),
                ('identifier', models.SlugField(blank=True, max_length=200, unique=True)),
                ('created_date', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
