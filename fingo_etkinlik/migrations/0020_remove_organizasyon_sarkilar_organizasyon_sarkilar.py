# Generated by Django 4.1.5 on 2023-10-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fingo_etkinlik', '0019_remove_organizasyon_sarkilar_organizasyon_sarkilar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizasyon',
            name='sarkilar',
        ),
        migrations.AddField(
            model_name='organizasyon',
            name='sarkilar',
            field=models.ManyToManyField(to='fingo_etkinlik.sarkilar'),
        ),
    ]
