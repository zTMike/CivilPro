# Generated by Django 5.0.2 on 2024-05-21 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='presupuesto',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
