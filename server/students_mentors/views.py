from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from .models import Mentor, Student, Recommended_QPs
from subscriptions.models import Subscriptions
from pydantic import BaseModel
from typing import List

# Pydantic models for data validation
class MentorCreationRequest(BaseModel):
    name: str
    email: str
    password: str
    phone: str

class StudentCreationRequest(BaseModel):
    name: str
    email: str
    password: str
    phone: str
    grade: int
    board: str
    mentor_id: int

class RecommendedQPRequest(BaseModel):
    mentor_id: int
    student_id: int
    qp_id: int
    is_done: bool
    recommended_time: str

class SubscriptionRequest(BaseModel):
    student_id: int
    sub_type: str
    start_date: str
    end_date: str

@require_POST
def create_mentor(request):
    if request.method == 'POST':
        mentor_data = MentorCreationRequest(**request.POST.dict())
        # Perform additional data validation if required
        mentor = Mentor(
            Name=mentor_data.name,
            Email=mentor_data.email,
            Password=mentor_data.password,
            Phone=mentor_data.phone
        )
        mentor.save()
        return JsonResponse({"message": "Mentor created successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})

@require_POST
def create_student(request):
    if request.method == 'POST':
        student_data = StudentCreationRequest(**request.POST.dict())
        # Perform additional data validation if required
        student = Student(
            Name=student_data.name,
            Email=student_data.email,
            Password=student_data.password,
            Phone=student_data.phone,
            Grade=student_data.grade,
            Board=student_data.board,
            Mentor_id=student_data.mentor_id
        )
        student.save()
        return JsonResponse({"message": "Student created successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})

@require_POST
def recommend_qp(request):
    if request.method == 'POST':
        recommended_qp_data = RecommendedQPRequest(**request.POST.dict())
        # Perform additional data validation if required
        recommended_qp = Recommended_QPs(
            MentorID_id=recommended_qp_data.mentor_id,
            StudentID_id=recommended_qp_data.student_id,
            QP_ID_id=recommended_qp_data.qp_id,
            isDone=recommended_qp_data.is_done,
            RecommendedTime=recommended_qp_data.recommended_time
        )
        recommended_qp.save()
        return JsonResponse({"message": "Question Paper recommended successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})

@require_POST
def subscribe_student(request):
    if request.method == 'POST':
        subscription_data = SubscriptionRequest(**request.POST.dict())
        # Perform additional data validation if required
        subscription = Subscriptions(
            UserID_id=subscription_data.student_id,
            Sub_Type=subscription_data.sub_type,
            SubscriptionStartDate=subscription_data.start_date,
            SubscriptionEndDate=subscription_data.end_date,
            isOver=False  # Default to False
        )
        subscription.save()
        return JsonResponse({"message": "Subscription created successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})
