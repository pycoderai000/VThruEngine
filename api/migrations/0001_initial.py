# Generated by Django 3.2.4 on 2021-06-08 19:33

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CartItems', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={})),
            ],
        ),
    ]
