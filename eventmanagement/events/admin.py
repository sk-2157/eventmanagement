from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','event_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('title',)
    search_fields = ('title','address','price','description','city','state','zipcode')
    list_per_page = 25
    

admin.site.register(Event, EventAdmin)

