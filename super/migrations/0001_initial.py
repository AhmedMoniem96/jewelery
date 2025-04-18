# Generated by Django 5.1.7 on 2025-04-09 01:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('imgc', models.ImageField(blank=True, null=True, upload_to='category_images')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('address', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('color_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('img', models.ImageField(blank=True, null=True, upload_to='color_images')),
            ],
            options={
                'db_table': 'color',
            },
        ),
        migrations.CreateModel(
            name='Suber',
            fields=[
                ('admin_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('password', models.BigIntegerField()),
            ],
            options={
                'db_table': 'suber',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=600)),
                ('img', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('price', models.BigIntegerField()),
                ('design', models.CharField(blank=True, max_length=400, null=True)),
                ('detail', models.CharField(blank=True, max_length=400, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='super.category')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='super.suber')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('pc_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='super.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='super.product')),
            ],
            options={
                'db_table': 'product_color',
            },
        ),
        migrations.CreateModel(
            name='ProductUser',
            fields=[
                ('pu_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='super.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='super.client')),
            ],
            options={
                'db_table': 'product_user',
            },
        ),
        migrations.AddField(
            model_name='color',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='super.suber'),
        ),
        migrations.AddField(
            model_name='category',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='super.suber'),
        ),
    ]
