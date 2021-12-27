from django.contrib import admin
from .models import Ads, Comment

# Register your models here.

# We want the admin UI to leave the picture and content_type alone


# Define the PicAdmin class
class AdsAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')


# Register the admin class with the associated model
admin.site.register(Ads, AdsAdmin)
admin.site.register(Comment)

