# Generated by Django 5.0.4 on 2024-04-20 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_remove_category_date_updated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='sub_total',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='tax',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='tax_amount',
        ),
    ]
