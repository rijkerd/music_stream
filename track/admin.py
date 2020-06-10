from django.contrib import admin
from .models import Track

admin.site.site_header = 'Music stream app'
admin.site.site_title = 'Music stream'


admin.site.register(Track)
