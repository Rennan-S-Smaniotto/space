from django.contrib import admin
from galeria.models import Fotografia

@admin.action(description="Marque as selecionadas como publicadas")
def marque_publicada(modeladmin, request, queryset):
    queryset.update(publicada=True)

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')
    list_display_links = ('id', 'nome', 'legenda')
    search_fields = ('nome', )
    list_filter = ('categoria', )
    list_editable = ('publicada', )
    actions = (marque_publicada, )
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)
