from django.contrib import admin
from .models import Book,Author,Address,Country

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name")

class AddressAdmin(admin.ModelAdmin):
    list_display=("street","postal_code","city")

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_filter=("author","rating")
    list_display = ("title","author")

class CountryAdmin(admin.ModelAdmin):
    list_display=("name","code")


admin.site.register(Author,AuthorAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Country,CountryAdmin)