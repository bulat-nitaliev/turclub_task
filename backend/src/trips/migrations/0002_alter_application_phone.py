# Generated by Django 5.1.8 on 2025-04-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]
