# Generated by Django 4.1.1 on 2022-09-29 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmfo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='productId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
