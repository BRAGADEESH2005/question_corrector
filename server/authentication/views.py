from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import User
from pydantic import BaseModel
from typing import Optional
from evaluators_qpuploaders import views as eq_views
from students_mentors import views as sm_views

# Pydantic model for data validation
class UserRegistrationRequest(BaseModel):
    name: str
    email: str
    password: str
    phone: str
    address: str
    role: str
    grade: Optional[int] = None
    board: Optional[str] = None
    mentor_id: Optional[int] = None

class UserLoginRequest(BaseModel):
    email: str
    password: str

@require_POST
def register_user(request):
    if request.method == 'POST':
        registration_data = UserRegistrationRequest(**request.POST.dict())
        # Perform additional data validation if required
        if len(registration_data.phone) != 10:
            return JsonResponse({"error": "Invalid phone number"})
        for char in registration_data.name:
            if char.isdigit():
                return JsonResponse({"error": "Name cannot contain numbers"})
        if len(registration_data.password) < 8:
            return JsonResponse({"error": "Password must be at least 8 characters long"})
        if registration_data.email.find('@') == -1 or registration_data.email.find('.') == -1:
            return JsonResponse({"error": "Invalid email"})
        user = User(
            Name=registration_data.name,
            Email=registration_data.email,
            Password=registration_data.password,
            Phone=registration_data.phone,
            Address=registration_data.address
        )
        user.save()
        if registration_data.role == 'evaluator':
            return eq_views.create_evaluator(request)
        elif registration_data.role == 'qp_uploader':
            return eq_views.create_qp_uploader(request)
        elif registration_data.role == 'student':
            return sm_views.create_student(request)
        elif registration_data.role == 'mentor':
            return sm_views.create_mentor(request)
        return JsonResponse({"message": "User registered successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})

@require_POST
def login_user(request):
    if request.method == 'POST':
        login_data = UserLoginRequest(**request.POST.dict())
        # Perform additional data validation if required
        try:
            user = User.objects.get(Email=login_data.email, Password=login_data.password)
            return JsonResponse({"message": "Login successful", "user_id": user.id})
        except User.DoesNotExist:
            return JsonResponse({"error": "Invalid email or password"})
    else:
        return JsonResponse({"error": "Invalid request method"})

def logout_user(request):
    # Implement logout logic if required
    return JsonResponse({"message": "Logout successful"})
