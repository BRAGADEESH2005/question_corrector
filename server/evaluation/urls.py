from django.urls import path
from .views import EvaluatedQuestionsListCreate, EvaluatedQuestionsRetrieveUpdateDestroy, EvaluationsListCreate, EvaluationsRetrieveUpdateDestroy

urlpatterns = [
    path('evaluatedquestions/', EvaluatedQuestionsListCreate.as_view(), name='evaluated_questions_list_create'),
    path('evaluatedquestions/<int:pk>/', EvaluatedQuestionsRetrieveUpdateDestroy.as_view(), name='evaluated_questions_retrieve_update_destroy'),
    path('evaluations/', EvaluationsListCreate.as_view(), name='evaluations_list_create'),
    path('evaluations/<int:pk>/', EvaluationsRetrieveUpdateDestroy.as_view(), name='evaluations_retrieve_update_destroy'),
]
