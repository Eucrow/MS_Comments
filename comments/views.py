from comments.models import Comment


class CommentListQuerySet(object):
    @staticmethod
    def get_comment_by_post(post_id):
        """
        Create the queryset with the comments list inside an post.
        :param id_post: Id from the post
        :return: Queryset with the comments order by publication date.
        """
        possible_comments = Comment.objects.all().filter(post_id=post_id)

        return possible_comments.order_by('-publication_datetime')  # possible_comments is a queryset


class NumberOfComments(object):
    @staticmethod
    def get_number_of_comments(post_id):
        """
        Get number of comments of a post
        :param id_post: Id from the post
        :return: integer with the number of comments from post_id
        """
        number_of_comments = Comment.objects.filter(post_id=post_id).count()

        return number_of_comments
