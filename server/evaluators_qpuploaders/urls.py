from django.urls import path
from .views import EvaluatorList, EvaluatorDetail, QP_UploaderList, QP_UploaderDetail, Eval_LanguagesList, Eval_LanguagesDetail, Eval_SubjectsList, Eval_SubjectsDetail, Eval_BoardsList, Eval_BoardsDetail, Question_PapersList, Question_PapersDetail, QP_StructureList, QP_StructureDetail

urlpatterns = [
    path('evaluators/', EvaluatorList.as_view(), name='evaluator_list'),
    path('evaluators/<int:pk>/', EvaluatorDetail.as_view(), name='evaluator_detail'),
    path('qp_uploaders/', QP_UploaderList.as_view(), name='qp_uploader_list'),
    path('qp_uploaders/<int:pk>/', QP_UploaderDetail.as_view(), name='qp_uploader_detail'),
    path('eval_languages/', Eval_LanguagesList.as_view(), name='eval_languages_list'),
    path('eval_languages/<int:pk>/', Eval_LanguagesDetail.as_view(), name='eval_languages_detail'),
    path('eval_subjects/', Eval_SubjectsList.as_view(), name='eval_subjects_list'),
    path('eval_subjects/<int:pk>/', Eval_SubjectsDetail.as_view(), name='eval_subjects_detail'),
    path('eval_boards/', Eval_BoardsList.as_view(), name='eval_boards_list'),
    path('eval_boards/<int:pk>/', Eval_BoardsDetail.as_view(), name='eval_boards_detail'),
    path('question_papers/', Question_PapersList.as_view(), name='question_papers_list'),
    path('question_papers/<int:pk>/', Question_PapersDetail.as_view(), name='question_papers_detail'),
    path('qp_structure/', QP_StructureList.as_view(), name='qp_structure_list'),
    path('qp_structure/<int:pk>/', QP_StructureDetail.as_view(), name='qp_structure_detail'),
]