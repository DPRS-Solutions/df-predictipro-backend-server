# Generated by Django 3.2.9 on 2023-08-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DF_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse', models.CharField(max_length=100)),
                ('product_Category', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
