from django.contrib import admin
from .models import Brand, Variant

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('BRDName', 'BRDDescription')
    search_fields = ('BRDName',)

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('VRTName', 'VRTDescription')
    search_fields = ('VRTName',)
