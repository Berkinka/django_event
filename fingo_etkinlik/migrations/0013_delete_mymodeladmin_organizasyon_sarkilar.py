# Generated by Django 4.1.5 on 2023-02-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fingo_etkinlik', '0012_mymodeladmin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModelAdmin',
        ),
        migrations.AddField(
            model_name='organizasyon',
            name='sarkilar',
            field=models.ManyToManyField(to='fingo_etkinlik.sarkilar'),
        ),
    ]
