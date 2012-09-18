from django.contrib import admin
from concepts.models import Card,Player,BitOfCardboard

#admin.site.register(BitOfCardboard)

class BitOfCardboardInline(admin.TabularInline):
    model = BitOfCardboard
    extra = 1
    
#class CardAdmin(admin.ModelAdmin):
#    inlines = (BitOfCardboardInline,)

class PlayerAdmin(admin.ModelAdmin):
    inlines = (BitOfCardboardInline,)

admin.site.register(Card)
admin.site.register(Player, PlayerAdmin)