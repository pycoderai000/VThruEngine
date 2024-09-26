from django.contrib import admin

from . import models


class CartAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(models.Cart,CartAdmin)