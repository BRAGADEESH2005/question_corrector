from django.urls import path
from . import views

urlpatterns = [
    path('evaluate_answer/', views.evaluate_answer),
    path('provide_feedback/', views.provide_feedback),
]
