# Generated by Django 4.0.4 on 2022-05-19 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0024_projeto_ano_alter_projeto_descricao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadeira',
            name='ects',
            field=models.IntegerField(null=True),
        ),
    ]
