from rest_framework import generics

from .models import Evaluated_Questions, Evaluations
from .serializers import EvaluatedQuestionsSerializer, EvaluationsSerializer

class EvaluationsListCreate(generics.ListCreateAPIView):
    queryset = Evaluations.objects.all()
    serializer_class = EvaluationsSerializer

class EvaluationsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluations.objects.all()
    serializer_class = EvaluationsSerializer

class EvaluatedQuestionsListCreate(generics.ListCreateAPIView):
    queryset = Evaluated_Questions.objects.all()
    serializer_class = EvaluatedQuestionsSerializer

class EvaluatedQuestionsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluated_Questions.objects.all()
    serializer_class = EvaluatedQuestionsSerializer
