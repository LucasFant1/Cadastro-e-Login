# Generated by Django 5.1.1 on 2024-09-28 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0003_usuario_descricao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='descricao',
        ),
    ]
