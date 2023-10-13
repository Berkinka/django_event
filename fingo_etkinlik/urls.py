from django.urls import path
from . import views

urlpatterns = [
    path("ekle/", views.ekle, name="ekle"),
    path("detay/<int:pk>/", views.organizasyondetay, name="detay"),
    path("guncelle/<int:pk_2>/", views.guncelle, name="guncelle"),
    path("sil/<int:pk_2>/", views.sil, name="sil"),
    path("organizasyonlar/", views.organizasyonlar, name="organizasyonlar"),
    path("", views.index, name="anasayfa"),
]