from django.contrib import admin
from .models import ForumPost, ForumComment, ForumReply, Events


admin.site.register(ForumPost)
admin.site.register(ForumComment)
admin.site.register(ForumReply)
admin.site.register(Events)
