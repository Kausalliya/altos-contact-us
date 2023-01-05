from django.contrib import admin

from contactapp.models import contactmodel, videomodel
# Register your models here.


@admin.register(contactmodel)
class contactAdmin(admin.ModelAdmin):
    list_display=('id','name','email','mobile','message')

@admin.register(videomodel)
class videoAdmin(admin.ModelAdmin):
    list_display=('id','video')