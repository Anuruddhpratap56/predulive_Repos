from django.contrib import admin
from media_coverage.models import news
from media_coverage.models import achievements

class admin_mediaCoverage(admin.ModelAdmin):
    list_display=('headLine','description','image')

admin.site.register(news,admin_mediaCoverage)

class admin_achievements(admin.ModelAdmin):
    list_display=('heading','description','image','date')
    
admin.site.register(achievements,admin_achievements)
