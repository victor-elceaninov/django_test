from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend


class ArticlesFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filterset = self.get_filterset(request, queryset, view)
        if view.action not in ['list'] or filterset is None:
            return queryset

        # Raise 404 in case when filter has invalid data
        if not filterset.is_valid() and self.raise_exception:
            raise Http404()
        return filterset.qs
