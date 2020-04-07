from django.contrib import admin
from .models import *
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
       # Register your models here.
       list_display = ['id','name','type',]
       search_fields = ['id','name','type']
       list_displays=['name','type']
       ordering = ['id']
       fields = ['id','name']
       readonly_fields = _fields = ['type']
#admin.site.register(Product,ProductAdmin)
admin.site.site_title='mydjango后台管理'
admin.site.site_head='mydjango'

