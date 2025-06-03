from django.contrib import admin
from web.models import Category, Product,Profile

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'image','gender')

admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'image', 'brand', 'category', 'comment_count',  'description', 'buy_count')
    list_filter = ('category',)
    search_fields = ('name',)

admin.site.register(Product,ProductAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ( 'user',)

admin.site.register(Profile,ProfileAdmin)

