from django.urls import path

from .views import SubscriptionsListCreate, SubscriptionsRetrieveUpdateDestroy

urlpatterns = [
    path('subscriptions/', SubscriptionsListCreate.as_view(), name='subscriptions_list_create'),
    path('subscriptions/<int:pk>/', SubscriptionsRetrieveUpdateDestroy.as_view(), name='subscriptions_retrieve_update_destroy'),
]