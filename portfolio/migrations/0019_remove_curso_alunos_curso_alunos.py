# Generated by Django 4.0.4 on 2022-05-19 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_rename_ola_cadeira_ranking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='alunos',
        ),
        migrations.AddField(
            model_name='curso',
            name='alunos',
            field=models.ManyToManyField(to='portfolio.pessoa'),
        ),
    ]
