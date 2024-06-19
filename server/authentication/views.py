from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import User
from pydantic import BaseModel

# Pydantic model for data validation
class UserRegistrationRequest(BaseModel):
    name: str
    email: str
    password: str
    phone: str
    address: str

class UserLoginRequest(BaseModel):
    email: str
    password: str

@require_POST
def register_user(request):
    if request.method == 'POST':
        registration_data = UserRegistrationRequest(**request.POST.dict())
        # Perform additional data validation if required
        user = User(
            Name=registration_data.name,
            Email=registration_data.email,
            Password=registration_data.password,
            Phone=registration_data.phone,
            Address=registration_data.address
        )
        user.save()
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
