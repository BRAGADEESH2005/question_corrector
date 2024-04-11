from rest_framework import serializers
from .models import Student, Mentor, Recommended_QPs

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'

class Recommended_QPsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommended_QPs
        fields = '__all__'