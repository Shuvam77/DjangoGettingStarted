from django.contrib import admin

from .models import Meeting, Room, Comment
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment


class MeetingAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Room)
admin.site.register(Comment)