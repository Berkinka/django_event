# Generated by Django 4.1.5 on 2023-02-21 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fingo_etkinlik', '0013_delete_mymodeladmin_organizasyon_sarkilar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizasyon',
            name='eklenme_tarih',
        ),
        migrations.RemoveField(
            model_name='organizasyon',
            name='org_tarih',
        ),
    ]
