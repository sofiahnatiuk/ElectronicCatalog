from django.urls import path
from .views import ComponentListView, ComponentDetailView

urlpatterns = [
    path('components/', ComponentListView.as_view(), name='component-list'),
    path('components/<int:pk>/', ComponentDetailView.as_view(), name='component-detail'),
]
