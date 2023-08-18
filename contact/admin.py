from django.contrib import admin
from contact.models import contact

class admin_contact(admin.ModelAdmin):
    list_display=('name','email','mobile','email_sub','description')


admin.site.register(contact,admin_contact)