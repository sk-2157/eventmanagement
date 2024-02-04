from django.contrib import admin
from .models import Participant

# Register your models here.
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('id','name','event','email','participated_date')
    list_display_links = ('id','name')
    search_fields = ('name','email','event')
    list_per_page = 25

admin.site.register(Participant, ParticipantAdmin)