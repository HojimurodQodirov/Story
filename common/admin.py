from django.contrib import admin
from .models import Post, DetailedInfo


class DetailedInfoInline(admin.StackedInline):
    model = DetailedInfo
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [DetailedInfoInline]
    list_display = ('title', 'detailed_info_url')

    def detailed_info_url(self, obj):
        return obj.get_detailed_info_url()

    detailed_info_url.short_description = 'Detailed Info URL'


@admin.register(DetailedInfo)
class DetailedInfoAdmin(admin.ModelAdmin):
    pass
