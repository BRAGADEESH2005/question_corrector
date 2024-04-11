from rest_framework import serializers
from .models import Evaluations, Evaluated_Questions

class EvaluatedQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluated_Questions
        fields = '__all__'

class EvaluationsSerializer(serializers.ModelSerializer):
    evaluated_questions = EvaluatedQuestionsSerializer(many=True)

    class Meta:
        model = Evaluations
        fields = '__all__'