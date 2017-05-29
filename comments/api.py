from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView

from comments.models import Comment
from comments.serializers import CommentSerializer, CommentListSerializer


class ListCreateCommentAPI(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # sobreescribimos el método get_serializer_class para que haga lo que nosotros deseamos,
    # en este caso devuelve PostSerializer si el método es POST o PostListSerializer si no.
    def get_serializer_class(self):
        return CommentSerializer if self.request.method == 'POST' else CommentListSerializer



