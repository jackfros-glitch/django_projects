from django.contrib import admin
from .models import Site, Category, Iso, State, Region
# Register your models here.

admin.site.register(Category)
admin.site.register(Iso)
admin.site.register(State)
admin.site.register(Region)

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','state','year', 'region']