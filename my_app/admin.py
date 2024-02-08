from django.contrib import admin

from my_app.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'preview', 'publish_time', 'is_publish', 'views')
    list_filter = ('is_publish',)
