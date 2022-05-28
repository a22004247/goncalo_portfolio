# Generated by Django 4.0.4 on 2022-05-17 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_remove_pessoa_linkcadeira_remove_pessoa_tipo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='linkLinkedin',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='linkLusofona',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='nome',
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('linkLusofona', models.CharField(max_length=200)),
                ('linkLinkedin', models.CharField(max_length=200)),
                ('professores', models.ManyToManyField(to='portfolio.pessoa')),
            ],
        ),
    ]
