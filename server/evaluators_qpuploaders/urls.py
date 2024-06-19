from django.urls import path
from . import views

urlpatterns = [
    path('register_evaluator/', views.create_evaluator),
    path('register_qpuploader/', views.create_qp_uploader),
    path('create_qp_structure/', views.create_question_paper),
]