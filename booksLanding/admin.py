from django.contrib import admin

from authentication.models import UserProfile 

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','phone')
    list_filter = ('user','phone')
    search_fields = ['user__username']