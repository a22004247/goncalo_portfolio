# Generated by Django 4.0.4 on 2022-05-25 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0043_alter_blog_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imagem',
            field=models.ImageField(blank=True, default='default.png', upload_to='blogeiros/'),
        ),
    ]
