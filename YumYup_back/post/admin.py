from django.contrib import admin

from post.models import Post, Ratings, Saved_post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('receipt_id', 'date', 'author_id')


@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'rating', 'comment', 'post_id')


@admin.register(Saved_post)
class Saved_postAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'post_id')




