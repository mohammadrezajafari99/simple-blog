from django.contrib import admin
from .models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)} ## همزمان فیلد پر میکنی فیلد دلخواه پر میشه



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)} ## همزمان فیلد پر میکنی فیلد دلخواه پر میشه

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)