from django.urls import path, include
from .views import UsersAPIView, AddUserAPI

urlpatterns = [
    path('', UsersAPIView.as_view(), name='users-list'),
    path('adduser/', AddUserAPI.as_view(), name='add_user'),
]