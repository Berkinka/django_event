# Generated by Django 4.1.5 on 2023-02-20 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fingo_etkinlik', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizasyon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eklenme_tarih', models.DateTimeField(auto_now_add=True, null=True)),
                ('org_tarih', models.DateField()),
                ('org_otel_adi', models.CharField(choices=[('ewi', 'Elite World Istanbul'), ('ewp', 'Elite World Prestige'), ('ewb', 'Elite World Business'), ('ewe', 'Elite World Europe'), ('ewa', 'Elite World Asia')], max_length=200)),
                ('org_tur', models.CharField(choices=[('dugun', 'DUGUN'), ('kina', 'KINA'), ('nisan', 'NISAN'), ('toplanti', 'TOPLANTI'), ('sunnet', 'SUNNET'), ('mezuniyet', 'MEZUNIYET'), ('diger', 'DIGER')], max_length=200)),
                ('gelin_ad_soyad', models.TextField(max_length=200)),
                ('damat_ad_soyad', models.TextField(max_length=200)),
                ('gelin_tel', models.TextField(max_length=200)),
                ('damat_tel', models.TextField(max_length=200)),
                ('gelin_bolge', models.TextField(max_length=200)),
                ('damat_bolge', models.TextField(max_length=200)),
                ('gelin_mail', models.TextField(max_length=200)),
                ('damat_mail', models.TextField(max_length=200)),
                ('verilen_fiyat', models.TextField(max_length=200)),
                ('salon', models.TextField(max_length=200)),
                ('kisi_sayisi', models.TextField(max_length=200)),
                ('sozlesme_yapildi', models.CharField(choices=[('yes', 'EVET'), ('no', 'HAYIR')], max_length=200)),
                ('paket_turu', models.CharField(choices=[('gumus', 'GUMUS PAKET'), ('altin', 'ALTIN PAKET'), ('pirlanta', 'PIRLANTA PAKET')], max_length=200)),
                ('notlar', models.TextField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
