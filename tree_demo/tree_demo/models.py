from django.db import models
from django_tree.models import BaseTreeNode


class Category(BaseTreeNode):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
