# Generated by Django 4.1.3 on 2022-11-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propostas', '0002_propostas_data_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propostas',
            name='data_pub',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='propostas',
            name='logo_proposta',
            field=models.URLField(),
        ),
    ]