from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display=["title","summery","user"]


# we can use 
#admin.site.register(Book)