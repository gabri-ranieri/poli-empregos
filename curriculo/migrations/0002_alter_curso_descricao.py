# Generated by Django 4.1.3 on 2022-11-29 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='descricao',
            field=models.CharField(max_length=255, null=True),
        ),
    ]