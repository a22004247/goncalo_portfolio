# Generated by Django 4.0.4 on 2022-05-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0051_alter_blog_descricao_alter_cadeira_linguagens'),
    ]

    operations = [
        migrations.CreateModel(
            name='TecnologiaUsada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usadas', models.ManyToManyField(to='portfolio.tecnologia')),
            ],
        ),
    ]
