# Generated by Django 3.2.7 on 2022-12-04 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productCRUD', '0002_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('nama_kategori', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('deskripsi', models.TextField()),
            ],
            options={
                'db_table': 'product_category',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='productCRUD.product_category'),
            preserve_default=False,
        ),
    ]
