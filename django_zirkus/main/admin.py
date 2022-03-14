from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ["link"]
    
    search_fields = ['title', 'body']
    list_display = (
        'title', 
        #'html_stripped_body', 
        # 'author', 
        'created_date'
        #,'image_tag'
    )
    fields = ['title', 'body', 'image'
    ]
    # This was used in fecobiome to override save method (or add to?) to automatically store author.
    # def save_model(self, request, obj, form, change):
    #     obj.author = request.user
    #     obj.save()

admin.site.register(Post, PostAdmin)