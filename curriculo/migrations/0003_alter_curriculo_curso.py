# Generated by Django 4.1.3 on 2022-11-29 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0002_alter_curso_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculo',
            name='curso',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='curriculo.curso'),
        ),
    ]
