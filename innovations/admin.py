from django.contrib import admin
from innovations.models import innovation

class admin_innovation(admin.ModelAdmin):
    list_display=('published_by','heading','date','image')
    
admin.site.register(innovation,admin_innovation)