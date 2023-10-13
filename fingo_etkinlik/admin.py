from django.contrib import admin

# Register your models here.

from .models import Organizasyon
from .models import Mekan_Adi
from .models import Org_Tur
from .models import Paket_Tur
from .models import Sarkilar
from .models import Sozlesme_Durumu
from .models import Sarki_Kategori

admin.site.register(Organizasyon)
admin.site.register(Mekan_Adi)
admin.site.register(Org_Tur)
admin.site.register(Paket_Tur)
admin.site.register(Sarkilar)
admin.site.register(Sozlesme_Durumu)
admin.site.register(Sarki_Kategori)
