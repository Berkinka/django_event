# Generated by Django 4.1.5 on 2023-02-21 16:10

from django.db import migrations, models
import django.db.models.deletion
import fingo_etkinlik.models


class Migration(migrations.Migration):

    dependencies = [
        ('fingo_etkinlik', '0008_alter_sarkilar_oncelik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizasyon',
            name='org_otel_adi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fingo_etkinlik.mekan_adi'),
        ),
        migrations.AlterField(
            model_name='organizasyon',
            name='org_tur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fingo_etkinlik.org_tur'),
        ),
        migrations.AlterField(
            model_name='organizasyon',
            name='paket_turu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fingo_etkinlik.paket_tur'),
        ),
        migrations.AlterField(
            model_name='sarkilar',
            name='oncelik',
            field=models.IntegerField(default=fingo_etkinlik.models.get_new_default, verbose_name='Öncelik'),
        ),
    ]