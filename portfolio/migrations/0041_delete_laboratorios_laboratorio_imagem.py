# Generated by Django 4.0.4 on 2022-05-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0040_laboratorios'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Laboratorios',
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='imagem',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
