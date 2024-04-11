from rest_framework import serializers
from .models import QP_Uploader, Evaluator, Eval_Languages, Eval_Subjects, Eval_Boards, Question_Papers, QP_Structure

class QP_UploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = QP_Uploader
        fields = '__all__'


class EvaluatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluator
        fields = '__all__'


class Eval_LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eval_Languages
        fields = '__all__'


class Eval_SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eval_Subjects
        fields = '__all__'


class Eval_BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eval_Boards
        fields = '__all__'


class Question_PapersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question_Papers
        fields = '__all__'


class QP_StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = QP_Structure
        fields = '__all__'