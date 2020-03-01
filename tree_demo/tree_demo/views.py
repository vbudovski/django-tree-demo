from typing import Dict
from typing import List

from django.views.generic import TemplateView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from tree_demo.models import Category


# DRF serializers are too slow for a large list.
def serialize_category(category: Category) -> Dict:
    return {
        'pk': category.pk,
        'name': category.name,
    }


def serialize_tree_node(tree_node: Dict) -> Dict:
    return {
        'node': serialize_category(tree_node['node']),
        'children': [serialize_tree_node(child) for child in tree_node['children'].values()],
    }


def serialize_tree(tree: Dict) -> List[Dict]:
    return [serialize_tree_node(tree_node) for tree_node in tree.values()]


class CategoryViewSet(ViewSet):
    def list(self, request):
        tree = Category.objects.build_tree()

        return Response(serialize_tree(tree))

    @action(detail=True, url_path='move-before', methods=['post'])
    def move_before(self, request, pk=None):
        node_to_move = Category.objects.get(pk=pk)
        node = Category.objects.get(pk=request.data.get('node'))

        Category.objects.insert_before(node, node_to_move)

        return Response()

    @action(detail=True, url_path='move-after', methods=['post'])
    def move_after(self, request, pk=None):
        node_to_move = Category.objects.get(pk=pk)
        node = Category.objects.get(pk=request.data.get('node'))

        Category.objects.insert_after(node, node_to_move)

        return Response()


class FrontendView(TemplateView):
    template_name = 'frontend.html'
