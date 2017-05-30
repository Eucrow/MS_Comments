from rest_framework import serializers

from rest_auth.serializers import UserDetailsSerializer

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')


# class CommentListSerializer(CommentSerializer):
#     class Meta(CommentSerializer.Meta):  # el PostSerializer.Meta dice que herede la clase Meta también del
#                                 # PostSerializer. Si no se pone, por defecto no la hereda
#         fields = ("comment", "post_id", "comment_author", "publication_datetime", "response_to")