# Generated by Django 4.1.2 on 2022-11-20 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_index_together_remove_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available',
        ),
    ]