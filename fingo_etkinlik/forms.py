from django.forms import ModelForm
from django import forms
from .models import Organizasyon
from .models import Sarkilar
from .models import Mekan_Adi
from .models import Sarki_Kategori
from datetime import date

today = date.today()

class Organizasyon_Ekleme_Formu(forms.ModelForm):
    class Meta:
        model = Organizasyon
        fields = '__all__'

    org_otel_adi = forms.ModelChoiceField(queryset=Mekan_Adi.objects.all())
    org_tarih = forms.DateField(widget=forms.TextInput(attrs={'min': '01-01-1900', 'value': today, 'type': 'date'}), required=True)
    gelin_ad_soyad = forms.CharField(max_length=200)
    damat_ad_soyad = forms.CharField(max_length=200)
    gelin_tel   = forms.CharField(max_length=200)
    damat_tel   = forms.CharField(max_length=200)
    gelin_bolge = forms.CharField(max_length=200)
    damat_bolge = forms.CharField(max_length=200)
    gelin_mail  = forms.CharField(max_length=200)
    damat_mail  = forms.CharField(max_length=200)
    kisi_sayisi = forms.CharField(max_length=200)
    verilen_fiyat = forms.CharField(max_length=200)
    salon = forms.CharField(max_length=200)
    kisi_sayisi = forms.CharField(max_length=200)
    notlar   = forms.CharField(max_length=200)
    sarkilar = forms.ModelMultipleChoiceField(
        queryset=Sarkilar.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class SarkiDuzenleme(forms.ModelForm):
    class Meta:
        model = Sarkilar
        fields = "__all__"

