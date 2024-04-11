from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user_list_create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user_retrieve_update_destroy'),
]