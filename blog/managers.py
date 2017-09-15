from django.db import models


class PostQuerySet(models.QuerySet):
    def display(self):
        return self.active()

    def active(self):
        return self.exclude(title__contains="Sample")

    def published(self):
        return self.filter(title__contains="post")


PostManager = models.Manager.from_queryset(PostQuerySet)
