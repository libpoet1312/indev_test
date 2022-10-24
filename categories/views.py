from rest_framework import generics

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
