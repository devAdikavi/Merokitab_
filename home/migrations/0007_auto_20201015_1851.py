# Generated by Django 3.0.6 on 2020-10-15 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]