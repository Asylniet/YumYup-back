from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
    )
    search_fields = ('email',)


admin.site.register(models.User, UserAdmin)
