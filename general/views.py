from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import ForumPost, ForumComment, ForumReply
from .serializers import ForumPostSerializer, UserSerializer, ForumCommentSerializer, ForumReplySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class ForumPostViewSet(viewsets.ModelViewSet):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        forum_post = ForumPost()
        forum_post.heading = request.data['heading']
        forum_post.body = request.data['body']
        forum_post.author = request.user
        forum_post.save()
        serializer = ForumPostSerializer(forum_post, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ForumCommentViewSet(viewsets.ModelViewSet):
    queryset = ForumComment.objects.all()
    serializer_class = ForumCommentSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        forum_comment = ForumComment()
        forum_comment.comment = request.data['comment']
        forum_comment.parent_post = request.data['post_id']
        forum_comment.author=request.user
        forum_comment.save()
        serializer = ForumCommentSerializer(forum_comment, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        forum_comment = ForumComment.objects.all().filter(parent_post = request.GET['post_id'])
        serializer = ForumCommentSerializer(forum_comment, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class ForumReplyViewSet(viewsets.ModelViewSet):
    queryset = ForumReply.objects.all()
    serializer_class = ForumReplySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        forum_reply = ForumReply()
        forum_reply.author = request.user
        forum_reply.parent_comment = request.data['comment_id']
        forum_reply.reply = request.data['reply']
        forum_reply.save()
        serializer = ForumReplySerializer(forum_reply, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        forum_reply = ForumReply.objects.all().filter(parent_comment = request.GET['comment_id'])
        serializer = ForumReplySerializer(forum_reply, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
