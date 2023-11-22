# Generated by Django 5.0rc1 on 2023-11-22 06:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=35)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Product Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=35)),
                ('description', models.CharField(max_length=255)),
                ('featured_image', models.ImageField(upload_to='products')),
                ('image_1', models.FileField(upload_to='images/products')),
                ('image_2', models.FileField(upload_to='images/products')),
                ('image_3', models.FileField(blank=True, null=True, upload_to='images/products')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('top_selling', models.BooleanField(default=False)),
                ('discount', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.productcategory')),
            ],
        ),
    ]
