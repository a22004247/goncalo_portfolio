# Generated by Django 4.0.4 on 2022-05-17 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_cadeira_curso_cadeira_linguagens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.curso'),
        ),
        migrations.RemoveField(
            model_name='cadeira',
            name='linguagens',
        ),
        migrations.AddField(
            model_name='cadeira',
            name='linguagens',
            field=models.ManyToManyField(to='portfolio.linguagem'),
        ),
    ]
