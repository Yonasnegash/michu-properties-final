# Generated by Django 4.1.4 on 2024-09-01 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_alter_listing_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
        ),
    ]
