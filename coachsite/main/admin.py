from django.contrib import admin
from main import models
# Register your models here.


class ForWhomAdmin(admin.ModelAdmin):
    list_display = ('for_whom', 'name_of_for_whom', 'time_update',)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone',)


class CustomerResultAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


class TariffsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


class UserReservationAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'phone',)


admin.site.register(models.ForWhom, ForWhomAdmin)
admin.site.register(models.CustomerResult, CustomerResultAdmin)
admin.site.register(models.Tariffs, TariffsAdmin)
admin.site.register(models.AboutMe, AboutMeAdmin)
admin.site.register(models.Contacts, ContactsAdmin)
admin.site.register(models.UserReservation, UserReservationAdmin)
