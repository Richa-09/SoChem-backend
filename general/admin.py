from django.contrib import admin
from .models import ForumPost, ForumComment, ForumReply


admin.site.register(ForumPost)
admin.site.register(ForumComment)
admin.site.register(ForumReply)

