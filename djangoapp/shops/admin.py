from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from djangoapp.shops.models import ItemToScrap, Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('name', 'url')
        return self.readonly_fields


@admin.register(ItemToScrap)
class ItemToScrapAdmin(admin.ModelAdmin):
    list_display = ('url', 'itemId', 'toScrap')
    fields = ('url', 'itemId', 'toScrap')


admin.site.unregister(User)
admin.site.unregister(Group)
