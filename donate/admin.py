from django.contrib import admin
from .models import donate
# Register your models here.

@admin.register(donate)
class donateAdmin(admin.ModelAdmin):
    list_display = ('amount', 'donate_to','name',"payment_status")
    list_filter = ('payment_status',)
    search_fields = ('name', 'donate_to')
    
