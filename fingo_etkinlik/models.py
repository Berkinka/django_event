from django.db import models
from django import forms
from django.db.models import Max
from django.forms import CheckboxSelectMultiple
from django.conf import settings
import datetime


def get_new_default():
    if Sarkilar.objects.all().count() == 0:
        new_order_default = 10
    else:
        new_order_default = Sarkilar.objects.all().aggregate(Max('oncelik'))['oncelik__max']+10
        return new_order_default

class Sarki_Kategori(models.Model):
    oncelik = models.IntegerField(verbose_name="Şarkı Kategorisi Önceliği")
    kategori_adi = models.TextField(verbose_name="Şarkı Kategorisi", max_length=200)
    class Meta:
        verbose_name = "Şarkı Kategorisi"
        verbose_name_plural = "Şarkı Kategorileri"

    def __str__(self):
        return self.kategori_adi


class Sarkilar(models.Model):
    oncelik = models.IntegerField(verbose_name="Öncelik", default = get_new_default)
    sarki_adi = models.TextField(verbose_name="Şarkı Adı", max_length=200)

    class Meta:
        verbose_name = 'Şarkı'
        verbose_name_plural = 'Şarkılar'

    def __str__(self):
        return self.sarki_adi
    

class Mekan_Adi(models.Model):
    mekan_adi = models.TextField(verbose_name='Mekan Adı', max_length=200)
    
    class Meta:
        verbose_name = 'Mekan Adı'
        verbose_name_plural = 'Mekan Adları'

    def __str__(self):
        return self.mekan_adi

class Org_Tur(models.Model):
    org_tur = models.TextField(verbose_name='Organizasyon Türü', max_length=200)

    class Meta:
        verbose_name = 'Organizasyon Türü'
        verbose_name_plural = 'Organizasyon Türleri'

    def __str__(self):
        return self.org_tur

class Paket_Tur(models.Model):
    paket_tur = models.TextField(verbose_name='Paket Türü', max_length=200)

    class Meta:
        verbose_name = 'Paket Türü'
        verbose_name_plural = 'Paket Türleri'

    def __str__(self):
        return self.paket_tur
    
class Sozlesme_Durumu(models.Model):
    sozlesme_yapildi = models.TextField(verbose_name='Sözleşme Yapıldı?', max_length=5)

    class Meta:
        verbose_name = 'Sözleşme Yapıldı?'
        verbose_name_plural = 'Sözleşme Yapıldı?'

    def __str__(self):
        return self.sozlesme_yapildi

class Organizasyon(models.Model):
    org_tarih = models.DateField()
    org_otel_adi = models.ForeignKey(Mekan_Adi, null=True, on_delete= models.SET_NULL)
    org_tur = models.ForeignKey(Org_Tur, null=True, on_delete= models.SET_NULL)
    gelin_ad_soyad = models.TextField(max_length=200)
    damat_ad_soyad = models.TextField(max_length=200)
    gelin_tel = models.TextField(max_length=200)
    damat_tel = models.TextField(max_length=200)
    gelin_bolge = models.TextField(max_length=200)
    damat_bolge = models.TextField(max_length=200)
    gelin_mail = models.TextField(max_length=200)
    damat_mail = models.TextField(max_length=200)
    kisi_sayisi = models.TextField(max_length=200)
    verilen_fiyat = models.TextField(max_length=200)
    salon = models.TextField(max_length=200)
    kisi_sayisi = models.TextField(max_length=200)
    sozlesme_yapildi = models.ForeignKey(Sozlesme_Durumu, null=True, on_delete= models.SET_NULL)
    paket_turu = models.ForeignKey(Paket_Tur, null=True, on_delete= models.SET_NULL)
    notlar = models.TextField(max_length=200)
    sarkilar = models.ManyToManyField(Sarkilar)

    class Meta:
        verbose_name = 'Organizasyon'
        verbose_name_plural = 'Organizasyonlar'

    def __str__(self):
        return f'{self.gelin_ad_soyad} ve {self.damat_ad_soyad}'

