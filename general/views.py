from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse
from .models import ForumPost, ForumComment, ForumReply, Events, UserExtension
from .serializers import ForumPostSerializer, UserSerializer, ForumCommentSerializer, ForumReplySerializer, EventsSerializer, UserExtensionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
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
        forum_post.author_name = request.user.first_name + ' ' + request.user.last_name
        forum_post.save()
        serializer = ForumPostSerializer(forum_post, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        if 'id' in request.GET:
            forum_post = ForumPost.objects.all().filter(author=request.GET['id'])
            serializer = ForumPostSerializer(forum_post, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            forum_post = ForumPost.objects.all().order_by('-id')
            serializer = ForumPostSerializer(forum_post, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)


class ForumCommentViewSet(viewsets.ModelViewSet):
    queryset = ForumComment.objects.all()
    serializer_class = ForumCommentSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        forum_comment = ForumComment()
        forum_comment.comment = request.data['comment']
        par_post = ForumPost.objects.all().filter(id=request.data['post_id'])
        forum_comment.parent_post = par_post[0]
        forum_comment.author = request.user
        forum_comment.author_name = request.user.first_name + ' ' + request.user.last_name
        forum_comment.save()
        serializer = ForumCommentSerializer(forum_comment, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        if 'post_id' in request.GET:
            forum_comment = ForumComment.objects.all().filter(parent_post = request.GET['post_id']).order_by('-id')
            serializer = ForumCommentSerializer(forum_comment, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            forum_comment = ForumComment.objects.all().filter(author = request.GET['user_id']).order_by('-id')
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


class UserFromTokenViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        user = Token.objects.get(key=request.data['token']).user
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

class UserExtensionViewSet(viewsets.ModelViewSet):
    queryset = UserExtension.objects.all()
    serializer_class = UserExtensionSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        user_details = UserExtension.objects.all().filter(user = request.GET['id'])
        serializer = UserExtensionSerializer(user_details, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

def commentCount(request):

    all_comment = ForumComment.objects.all()
    user = User.objects.get(id = request.GET['user_id']).username
    count = 0
    for comment in all_comment:
        parent_post = comment.parent_post
        if str(parent_post.author) == str(user):
            count = count + 1
    print((count))
    return HttpResponse({count}, status=status.HTTP_200_OK)