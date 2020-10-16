from django.urls import path, include
from rest_framework import routers
from .views import ForumPostViewSet, ForumCommentViewSet, ForumReplyViewSet, UserViewSet, UserFromTokenViewSet, EventsViewSet
from django.conf.urls.static import static
from django.conf import settings
router = routers.DefaultRouter()

router.register('forum-post', ForumPostViewSet)
router.register('forum-comment', ForumCommentViewSet)
router.register('forum-reply', ForumReplyViewSet)
router.register('users', UserViewSet)
router.register('user-from-token', UserFromTokenViewSet)
router.register('events', EventsViewSet)

urlpatterns = [
   path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
