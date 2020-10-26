from django.contrib import admin
from .models import Article, Comment

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine
    ]

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)