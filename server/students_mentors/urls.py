from django.urls import path
from .views import StudentListCreate, StudentRetrieveUpdateDestroy, MentorListCreate, MentorRetrieveUpdateDestroy, RecommendedQPsListCreate, RecommendedQPsRetrieveUpdateDestroy

urlpatterns = [
    path('students/', StudentListCreate.as_view(), name='student_list_create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroy.as_view(), name='student_retrieve_update_destroy'),
    path('mentors/', MentorListCreate.as_view(), name='mentor_list_create'),
    path('mentors/<int:pk>/', MentorRetrieveUpdateDestroy.as_view(), name='mentor_retrieve_update_destroy'),
    path('recommended_qps/', RecommendedQPsListCreate.as_view(), name='recommended_qps_list_create'),
    path('recommended_qps/<int:pk>/', RecommendedQPsRetrieveUpdateDestroy.as_view(), name='recommended_qps_retrieve_update_destroy'),
]