from django.contrib import admin
from campaigns.models import campaigns

class admin_campaigns(admin.ModelAdmin):
    list_display=('day','m_y','heading','description','image')
    
admin.site.register(campaigns,admin_campaigns)


