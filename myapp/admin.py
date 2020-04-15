from django.contrib import admin
from .models import Concert, Singer, Ticket_price,FavoriteConcert,Photo
# Register your models here.

class ConcertInline(admin.TabularInline):
    """docstring for ConcertInline"""
    model = Concert
    extra = 3

class SingerAdmin(admin.ModelAdmin):
    fields = ('name','category','region', 'language')
    inlines = [ConcertInline]
    list_display = ('name', 'category','region', 'language')
    list_filter = ['category']
    search_fields = ['name']

class Ticket_priceInline(admin.StackedInline):
    model = Ticket_price
    extra = 3

class Launch_timeInline(admin.StackedInline):
    """docstring for Launch_timeInline"""
   
    extra = 3

class ConcertAdmin(admin.ModelAdmin):
    list_display = ('concert_name', 'singer','buy_ticket_date', 'votes')   

admin.site.register(Singer,SingerAdmin)
admin.site.register(Concert,ConcertAdmin)
admin.site.register(FavoriteConcert)
admin.site.register(Photo)
