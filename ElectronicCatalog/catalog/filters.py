import django_filters
from .models import Component


class ComponentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Component
        fields = ['name']
