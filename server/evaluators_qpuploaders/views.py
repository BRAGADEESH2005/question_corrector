from rest_framework import generics

from .models import Evaluator, QP_Uploader, Eval_Languages, Eval_Subjects, Eval_Boards, Question_Papers, QP_Structure
from .serializers import EvaluatorSerializer, QP_UploaderSerializer, Eval_LanguagesSerializer, Eval_SubjectsSerializer, Eval_BoardsSerializer, Question_PapersSerializer, QP_StructureSerializer

class EvaluatorList(generics.ListCreateAPIView):
    queryset = Evaluator.objects.all()
    serializer_class = EvaluatorSerializer

class EvaluatorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluator.objects.all()
    serializer_class = EvaluatorSerializer

class QP_UploaderList(generics.ListCreateAPIView):
    queryset = QP_Uploader.objects.all()
    serializer_class = QP_UploaderSerializer

class QP_UploaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QP_Uploader.objects.all()
    serializer_class = QP_UploaderSerializer

class Eval_LanguagesList(generics.ListCreateAPIView):
    queryset = Eval_Languages.objects.all()
    serializer_class = Eval_LanguagesSerializer

class Eval_LanguagesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eval_Languages.objects.all()
    serializer_class = Eval_LanguagesSerializer

class Eval_SubjectsList(generics.ListCreateAPIView):
    queryset = Eval_Subjects.objects.all()
    serializer_class = Eval_SubjectsSerializer

class Eval_SubjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eval_Subjects.objects.all()
    serializer_class = Eval_SubjectsSerializer

class Eval_BoardsList(generics.ListCreateAPIView):
    queryset = Eval_Boards.objects.all()
    serializer_class = Eval_BoardsSerializer

class Eval_BoardsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eval_Boards.objects.all()
    serializer_class = Eval_BoardsSerializer

class Question_PapersList(generics.ListCreateAPIView):
    queryset = Question_Papers.objects.all()
    serializer_class = Question_PapersSerializer

class Question_PapersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question_Papers.objects.all()
    serializer_class = Question_PapersSerializer

class QP_StructureList(generics.ListCreateAPIView):
    queryset = QP_Structure.objects.all()
    serializer_class = QP_StructureSerializer

class QP_StructureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QP_Structure.objects.all()
    serializer_class = QP_StructureSerializer