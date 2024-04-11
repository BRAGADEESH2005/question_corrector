from rest_framework import generics

from .models import Student, Mentor, Recommended_QPs
from .serializers import StudentSerializer, MentorSerializer, Recommended_QPsSerializer

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class MentorListCreate(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class RecommendedQPsListCreate(generics.ListCreateAPIView):
    queryset = Recommended_QPs.objects.all()
    serializer_class = Recommended_QPsSerializer

class RecommendedQPsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recommended_QPs.objects.all()
    serializer_class = Recommended_QPsSerializer