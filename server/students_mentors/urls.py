from django.urls import path
from . import views

urlpatterns = [
    path('create_mentor/', views.create_mentor, name='create_mentor'),
    path('create_student/', views.create_student, name='create_student'),
    path('recommend_qp/', views.recommend_qp, name='recommend_qp'),
    path('subscribe_student/', views.subscribe_student, name='subscribe_student'),
]