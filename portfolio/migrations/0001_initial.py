# Generated by Django 4.0.4 on 2022-05-09 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=30)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('imagem', models.ImageField(upload_to=None)),
            ],
        ),
    ]
