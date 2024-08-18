from django.contrib import admin
from .models import Author,Post,Tag

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    fields=('first_name','last_name','email')

class PostAdmin(admin.ModelAdmin):
    fields=('author','title','excerpt','image_name','date','slug','content')
    list_selected_related=['author','tag']
    list_filter=['author','title','date']

class TagAdmin(admin.ModelAdmin):
    fields=('posts','caption',)

admin.site.register(Author,AuthorAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)