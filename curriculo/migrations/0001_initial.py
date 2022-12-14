# Generated by Django 4.1.3 on 2022-11-29 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0004_remove_empresa_email_remove_estudante_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Curriculo',
            fields=[
                ('estudante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.estudante')),
                ('bio', models.TextField(null=True)),
                ('foto', models.URLField(null=True)),
                ('profissional', models.TextField(null=True)),
                ('academico', models.TextField(null=True)),
                ('experiencia', models.TextField(null=True)),
                ('curso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='curriculo.curso')),
            ],
        ),
    ]
