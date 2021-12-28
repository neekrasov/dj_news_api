from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category, Review, Rating, RatingStar


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src = "{obj.photo.url}" width = "75">')
        else:
            return 'Фото не установлено'

    get_photo.short_desctiption = "Миниатура"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "text", "news")
    list_display_links = ("name",)
    search_fields = ("email", "news")
    list_filter = ("news",)


class RatingStarAdmin(admin.ModelAdmin):
    list_display = ("value",)


class RatingAdmin(admin.ModelAdmin):
    list_display = ("ip", "star", "news")


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(RatingStar, RatingStarAdmin)
admin.site.register(Rating, RatingAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
