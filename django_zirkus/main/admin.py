from django.contrib import admin
from .models import Post, Details

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ["link"]
    
    search_fields = ['admin_name', 'title', 'body']
    list_display = (
        'admin_name',
        # 'mandatory',
        'title', 
        #'html_stripped_body', 
        # 'author', 
        'created_date'
        #,'image_tag'
    )
    fields = ['admin_name', 'mandatory', 'title', 'body', 'image'
    ]
    # This was used in fecobiome to override save method (or add to?) to automatically store author.
    # def save_model(self, request, obj, form, change):
    #     obj.author = request.user
    #     obj.save()
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        if obj:
            if obj.mandatory == True:
                return False
            else:
                return True

class DetailsAdmin(admin.ModelAdmin):

    # list_display = ['address', 'phone', 'email', 'insta', 'facebook']
    fields = ['address', 'phone', 'email', 'insta', 'facebook']
    list_display = ['address', 'phone', 'email', 'insta', 'facebook']
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Post, PostAdmin)
admin.site.register(Details, DetailsAdmin)