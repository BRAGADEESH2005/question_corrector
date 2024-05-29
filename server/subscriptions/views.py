from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Subscriptions
from pydantic import BaseModel

# Pydantic model for data validation
class SubscriptionRequest(BaseModel):
    student_id: int
    sub_type: str
    start_date: str
    end_date: str

@require_POST
def create_subscription(request):
    if request.method == 'POST':
        subscription_data = SubscriptionRequest(**request.POST.dict())
        # Perform additional data validation if required
        subscription = Subscriptions(
            student_id=subscription_data.student_id,
            sub_type=subscription_data.sub_type,
            start_date=subscription_data.start_date,
            end_date=subscription_data.end_date
        )
        subscription.save()
        return JsonResponse({"message": "Subscription created successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})
