from django.contrib import admin
from embed_video.admin import AdminVideoMixin
# Register your models here.
from .models import *

# admin.site.register(Movie)

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Movie, MyModelAdmin)
admin.site.register(Review)
