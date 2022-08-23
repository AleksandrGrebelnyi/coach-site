from django.contrib import admin
from main import models
# Register your models here.


class ForWhomAdmin(admin.ModelAdmin):
    list_display = ('for_whom', 'name_of_for_whom', 'time_update',)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone',)


admin.site.register(models.ForWhom, ForWhomAdmin)
admin.site.register(models.CustomerResult)
admin.site.register(models.Tariffs)
admin.site.register(models.AboutMe)
admin.site.register(models.Contacts, ContactsAdmin)
