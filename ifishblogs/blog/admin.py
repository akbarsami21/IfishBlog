from django.contrib import admin
from .models import Category,Post
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','catId','title','description','url','addDate',)
    search_fields=('title',)
    list_filter=('title',)
    list_per_page=10

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('image_tag','postId','title','content','url','cat','addDate',)
    search_fields=('title',)
    list_filter=('cat',)
    list_per_page=10

