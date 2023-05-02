from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('receipt_id', 'date', 'author_id')
#
#
# @admin.register(Rating)
# class RatingAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'rating', 'comment', 'post_id ')
#
#
# @admin.register(Saved_post)
# class Saved_postAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'post_id ')

# admin.site.register(Post)
admin.site.register(Rating)
admin.site.register(Saved_post)