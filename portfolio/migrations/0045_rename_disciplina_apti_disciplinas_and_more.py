# Generated by Django 4.0.4 on 2022-05-25 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0044_alter_blog_imagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apti',
            old_name='Disciplina',
            new_name='disciplinas',
        ),
        migrations.RenameField(
            model_name='apti',
            old_name='Projeto',
            new_name='projetos',
        ),
    ]
