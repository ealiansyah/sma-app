# Generated by Django 3.2.7 on 2022-12-04 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkout',
            options={'ordering': ['created_at']},
        ),
    ]
