from typing import Optional

from django.core.management import BaseCommand
from django.db import transaction

from tree_demo.models import Category


class Command(BaseCommand):
    @transaction.atomic
    def add_children(self, parent: Optional[Category], depth: int, max_depth: int, nodes_per_level: int):
        if parent is None:
            prefix = ''
        else:
            prefix = f'{parent.name}_'

        nodes = []
        for i in range(nodes_per_level):
            try:
                previous = nodes[i - 1]
            except IndexError:
                previous = None

            new_node = Category.objects.create(name=f'{prefix}{i}', parent=parent, previous=previous)
            nodes.append(new_node)

        if depth < max_depth:
            for node in nodes:
                self.add_children(node, depth + 1, max_depth, nodes_per_level)

    @transaction.atomic
    def handle(self, *args, **options):
        self.add_children(None, 0, 3, 10)
