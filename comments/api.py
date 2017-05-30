from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from comments.models import Comment
from comments.permissions import CommentPermission
from comments.serializers import CommentSerializer
from comments.views import CommentListQuerySet, NumberOfComments


class CreateCommentAPI(CreateAPIView):
    permission_classes = (CommentPermission,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ListCommentAPI(ListAPIView):
    authentication_classes = ()
    permission_classes = (CommentPermission,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        comments_by_post = CommentListQuerySet.get_comment_by_post(post_id=self.kwargs.get('url'))
        queryset = comments_by_post

        return queryset


class NumberOfCommentsAPI(APIView):
    authentication_classes = ()
    permission_classes = (CommentPermission,)

    def get(self, request, post_id):
        number_of_comments = NumberOfComments.get_number_of_comments(post_id=post_id)

        context = {"number_of_comments": number_of_comments}

        return Response(context, status=HTTP_200_OK)
