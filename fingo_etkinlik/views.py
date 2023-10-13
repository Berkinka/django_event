from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *
from .utils import ilksayi
from .forms import Organizasyon_Ekleme_Formu
from .forms import SarkiDuzenleme
from datetime import date
from dateutil.relativedelta import *
from django.utils.timezone import now




def index(request):
  tarih = date.today()
  organizasyonlar = Organizasyon.objects.all()
  yakinda = Organizasyon.objects.filter(org_tarih__gte=tarih).order_by('org_tarih')
  ilk_gun = tarih.replace(day=1)
  son_gun = tarih + relativedelta(day=31)
  bu_ay_is_adeti = Organizasyon.objects.filter(org_tarih__range=[ilk_gun, son_gun]).count()
  sozlesme_evet = Organizasyon.objects.filter(sozlesme_yapildi__sozlesme_yapildi__contains="EVET").count()
  sozlesme_hayir = Organizasyon.objects.filter(sozlesme_yapildi__sozlesme_yapildi__contains="HAYIR").count()
  return render(request, 'index.html', {'is': organizasyonlar, 'yakinda_is': yakinda, 'bu_ay': bu_ay_is_adeti, 'sozlesme_evet_adet': sozlesme_evet, 'sozlesme_hayir_adet': sozlesme_hayir})

def organizasyondetay(request, pk):
  detay_cek = Organizasyon.objects.get(id=pk)
  context = {'detay_cek':detay_cek}
  return render(request, 'organizasyondetay.html', context)

def ekle(request):
  form = Organizasyon_Ekleme_Formu()
  if request.method == 'POST':
    form = Organizasyon_Ekleme_Formu(request.POST or None)
    if form.is_valid():
      deger = form.save()
      messages.success(request, 'Organizasyon başarıyla eklenmiştir.')
      return redirect('detay', deger.pk)
  context = {'form':form}
  return render(request, 'org_ekle.html', context)

def guncelle(request, pk_2):
  organizasyon = Organizasyon.objects.get(id=pk_2)
  form = Organizasyon_Ekleme_Formu(instance=organizasyon)
  if request.method == 'POST':
    form = Organizasyon_Ekleme_Formu(request.POST or None ,instance=organizasyon)
    if form.is_valid():
      form.save(commit=False)
      form.save()
      messages.success(request, 'Organizasyon başarıyla güncellenmiştir.')
      return redirect('detay', pk_2)
    else:
      print("Invalid Form")
      print(form.errors)

  context = {'form':form}
  return render(request, 'org_ekle.html', context)

def sil(request, pk_2):
  organizasyon = Organizasyon.objects.get(id=pk_2)
  context = {'org_adi':organizasyon}
  if request.method == "POST":
    organizasyon.delete()
    return redirect('/')
  return render(request, 'sil.html', context)

def sorgu_gecerli(deger):
  return deger != '' and deger != 'Tüm Oteller' and deger is not None
  
def organizasyonlar(request):
  organizasyonlar = Organizasyon.objects.all()
  otel_adlari = Mekan_Adi.objects.all()
  kategori_secimi = request.GET.get('kategori')
  id_cikar = None

  if sorgu_gecerli(kategori_secimi):
    id_cikar = Mekan_Adi.objects.only('id').get(mekan_adi=kategori_secimi).id
  

  if sorgu_gecerli(kategori_secimi):
    organizasyonlar = organizasyonlar.filter(org_otel_adi__mekan_adi__icontains=kategori_secimi)


  return render(request, 'organizasyonlar.html', {'is': organizasyonlar, 'otel_adlari': otel_adlari, 'kategori_secimi': kategori_secimi, 'id_cikar': id_cikar})