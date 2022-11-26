from django.contrib import admin
from .models import Thread, Reply


class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'created', 'id']
    search_fields = ['title']



class ReplyAdmin(admin.ModelAdmin):
    list_display = ['reply', 'created', 'id', 'thread']
    search_fields = ['reply']

admin.site.register(Thread, ThreadAdmin)
admin.site.register(Reply, ReplyAdmin)
