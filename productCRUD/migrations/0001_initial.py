# Generated by Django 4.1 on 2022-12-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=63)),
                ('description', models.CharField(max_length=127)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('barcode_id', models.CharField(max_length=127, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
