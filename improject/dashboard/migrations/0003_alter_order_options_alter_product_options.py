# Generated by Django 4.2.16 on 2024-12-02 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Ordenes'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Productos'},
        ),
    ]
