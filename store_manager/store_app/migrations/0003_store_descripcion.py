# Generated by Django 4.1.1 on 2023-12-10 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0002_alter_store_nombre_alter_store_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='descripcion',
            field=models.CharField(default='Cerveza ...', max_length=300),
        ),
    ]
