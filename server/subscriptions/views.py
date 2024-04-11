from rest_framework import generics

from .models import Subscriptions
from .serializers import SubscriptionsSerializer

class SubscriptionsListCreate(generics.ListCreateAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer

class SubscriptionsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer