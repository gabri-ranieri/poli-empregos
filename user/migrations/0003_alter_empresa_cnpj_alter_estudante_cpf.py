# Generated by Django 4.1.3 on 2022-11-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_empresa_email_alter_estudante_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='cnpj',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='cpf',
            field=models.CharField(max_length=20),
        ),
    ]
