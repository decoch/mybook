from django.contrib import admin

# -*- coding: utf-8 -*-
from django.contrib import admin
from cms.models import Book, Impression

# admin.site.register(Book)
# admin.site.register(Impression)

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publisher', 'page',) # 一覧に出したい項目
    list_display_link = ('id', 'name',) # 修正リンクでクリックできる項目
admin.site.register(Book, BookAdmin)

class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_link = ('id', 'commnet',)
admin.site.register(Impression, ImpressionAdmin)
