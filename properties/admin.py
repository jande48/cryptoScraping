from django.contrib import admin
from .models import Property, YieldlyToAlgoRatio
# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    fields = ('data', 'currency','date')
    list_display = ['data', 'currency','date']

@admin.register(YieldlyToAlgoRatio)
class YieldlyToAlgoRatioAdmin(admin.ModelAdmin):
    fields = ('ratio', 'date')
    list_display = ['ratio', 'date']
