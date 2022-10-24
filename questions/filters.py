from rest_framework.filters import BaseFilterBackend


class MyCustomFilter(BaseFilterBackend):
    """
    Custom filters that implements filtering based on query params.
    Each query param could have multiple values that are comma-separated!
    """
    def filter_queryset(self, request, queryset, view):
        categories = request.query_params.get('category')
        difficulty = request.query_params.get('difficulty')

        if categories:
            categories = categories.split(',')
            queryset = queryset.filter(category__in=categories)

        if difficulty:
            difficulty = difficulty.split(',')
            queryset = queryset.filter(difficulty__in=difficulty)

        return queryset
