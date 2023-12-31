from django.urls import path
from .views import GadgetListView, GadgetDetailView

urlpatterns = [
    path('', GadgetListView.as_view(), name='gadget_list'),
    path('<int:pk>/', GadgetDetailView.as_view(), name='gadget_detail'),
]
