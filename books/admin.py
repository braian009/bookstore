# books/admin.py

from django.contrib import admin
from .models import Book, Review
from django.contrib.admin import TabularInline

# Register your models here.


class ReviewInline(TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price',)
    inlines = [
        ReviewInline,
    ]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'author',)


admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
