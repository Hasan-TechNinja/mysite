from django.contrib import admin
from . models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'slug', 'body', 'created', 'updated', 'status'
    )

    actions = ['Enable', 'Disable']

    @admin.action(description="Enable")
    def Enable(self, request, status):
        status.update(status = "True")
    
    @admin.action(description="Disable")
    def Disable(self, request, status):
        status.update(status = "False")
        
admin.site.register(Blog, BlogAdmin)