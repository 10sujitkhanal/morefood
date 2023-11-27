from django.urls import path
from .views import MenuAPIView

urlpatterns = [
    path('menus/', MenuAPIView.as_view(), name='menu-list'),
    # path('menus/<int:pk>/', MenuAPIView.as_view(), name='menu-detail'),
]
