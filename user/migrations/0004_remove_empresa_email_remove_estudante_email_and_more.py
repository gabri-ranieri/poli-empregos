# Generated by Django 4.1.3 on 2022-11-27 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_empresa_cnpj_alter_estudante_cpf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='email',
        ),
        migrations.RemoveField(
            model_name='estudante',
            name='email',
        ),
        migrations.AlterField(
            model_name='estudante',
            name='cpf',
            field=models.CharField(max_length=2),
        ),
    ]