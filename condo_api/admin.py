from django.contrib import admin

from .models import Condominio, Apartamento, Tag, ControleDeAcesso

admin.site.register(Condominio)

admin.site.register(Apartamento)

admin.site.register(Tag)

admin.site.register(ControleDeAcesso)
