

from django.db import models


class Comment(models.Model):
    # the post_id field received is the id field from posts model.
    post_id = models.PositiveIntegerField(blank=False)
    comment = models.TextField(blank=False)
    # The response_to field is the comment id which is responded.
    # If response_to is 0, means that is commented directly to the post.
    # Else, the comment is a response to another comment,
    response_to = models.PositiveIntegerField(blank=True)
    publication_datetime = models.DateTimeField(auto_now_add=True)
    comment_author = models.TextField(blank=False)

    def __str__(self):
        return str(self.title)
