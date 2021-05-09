from django.contrib import admin

# Register your models here.
from .models import Post,PostPoint
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','short-description',)
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')

@admin.register(PostPoint)
class PostPointAdmin(admin.ModelAdmin):
    list_display = ('post','post_point_text')

