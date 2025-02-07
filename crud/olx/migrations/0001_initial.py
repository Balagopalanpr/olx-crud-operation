# Generated by Django 5.0.6 on 2024-05-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.IntegerField()),
                ('year_reg', models.CharField(max_length=50)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='olx/media')),
                ('product_desc', models.CharField(max_length=50)),
            ],
        ),
    ]
