from django.db import models
from django_comments.abstracts import BaseCommentAbstractModel


class CommentForPublication(BaseCommentAbstractModel):
    """Comment for user's publication object."""
    comment = models.TextField(max_length=5000)
