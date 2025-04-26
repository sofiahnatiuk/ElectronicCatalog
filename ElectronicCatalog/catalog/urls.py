from django.urls import path
from .views import (
    ComponentListView,
    ComponentDetailView,
    ComponentCreateView,
    ComponentUpdateView,
    ComponentDeleteView
)

urlpatterns = [
    path('components/', ComponentListView.as_view(), name='component-list'),
    path('components/<int:pk>/', ComponentDetailView.as_view(), name='component-detail'),
    path('components/create/', ComponentCreateView.as_view(), name='component-create'),
    path('components/<int:pk>/update/', ComponentUpdateView.as_view(), name='component-update'),
    path('components/<int:pk>/delete/', ComponentDeleteView.as_view(), name='component-delete'),
]
