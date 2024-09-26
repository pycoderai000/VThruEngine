from django.contrib import admin

from . import models
from django.contrib.auth.admin import UserAdmin

class UserPanelAdmin(UserAdmin):
    ordering = ('email',)
    #exclude = ('username','password')
    list_display = ('id',"email","image","phone_number","is_active","is_staff","is_superuser")

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        perm_fields = ('is_active', 'is_staff', 'is_superuser')
        return [
                (('Personal info'), {'fields':('email','password','image','phone_number')}),
                (('Permissions'), {'fields': perm_fields})]
        
    add_fieldsets = (
        (None, {
            'fields': ("email",'password1','password2',"name","image","phone_number","verified","receive_updates_on_notifications","receive_updates_on_email","receive_updates_on_sms","receive_offers_on_notifications","receive_offers_on_email","receive_offers_on_sms","cart",'is_active','is_staff'),
        }),
    )


admin.site.register(models.CustomUser,UserPanelAdmin)