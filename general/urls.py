from django.urls import path, include
from rest_framework import routers
from .views import ForumPostViewSet, ForumCommentViewSet, ForumReplyViewSet
router = routers.DefaultRouter()

router.register('forum-post', ForumPostViewSet)
router.register('forum-comment', ForumCommentViewSet)
router.register('forum-reply', ForumReplyViewSet)

urlpatterns = [
   path('', include(router.urls)),
]