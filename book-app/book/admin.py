from django.contrib import admin

from .models import Category, Book

#追加
class BookAdmin(admin.ModelAdmin):
    list_display=('pk','title','author','publisher','buydate','category','url','rental','email','memo','comment')

admin.site.register(Category)
admin.site.register(Book,BookAdmin)       #修正
