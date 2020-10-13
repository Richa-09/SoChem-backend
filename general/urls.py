from django.urls import path, include
from rest_framework import routers
from .views import ForumPostViewSet, ForumCommentViewSet, ForumReplyViewSet, UserViewSet
router = routers.DefaultRouter()

router.register('forum-post', ForumPostViewSet)
router.register('forum-comment', ForumCommentViewSet)
router.register('forum-reply', ForumReplyViewSet)
router.register('users', UserViewSet)

urlpatterns = [
   path('', include(router.urls)),
]