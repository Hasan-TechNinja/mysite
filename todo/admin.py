from django.contrib import admin
from . models import Database

# Register your models here.


class DatabaseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description'
    )
admin.site.register(Database, DatabaseAdmin)