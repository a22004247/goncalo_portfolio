# Generated by Django 4.0.4 on 2022-05-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0052_tecnologiausada'),
    ]

    operations = [
        migrations.CreateModel(
            name='PadroesUsados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
    ]
