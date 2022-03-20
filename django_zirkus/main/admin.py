from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ["link"]
    
    search_fields = ['admin_name', 'title', 'body']
    list_display = (
        'admin_name',
        'title', 
        #'html_stripped_body', 
        # 'author', 
        'created_date'
        #,'image_tag'
    )
    fields = ['admin_name', 'title', 'body', 'image'
    ]
    # This was used in fecobiome to override save method (or add to?) to automatically store author.
    # def save_model(self, request, obj, form, change):
    #     obj.author = request.user
    #     obj.save()
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        if obj:
            if "Kort" in obj.admin_name or "Footer" in obj.admin_name:
                return False
            else:
                return True

admin.site.register(Post, PostAdmin)