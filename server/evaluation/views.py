from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Evaluations, Evaluated_Questions
from pydantic import BaseModel

# Pydantic models for data validation
class EvaluationRequest(BaseModel):
    student_id: int
    evaluator_id: int
    evaluation_id: str
    paper_id: int
    marks: int
    upload_time: str
    student_rating: int
    evaluator_rating: int

class FeedbackRequest(BaseModel):
    evaluation_id: str
    qp_id: int
    group_marks: int
    question_number: str
    marks: int
    feedback: str

@require_POST
def evaluate_answer(request):
    if request.method == 'POST':
        evaluation_data = EvaluationRequest(**request.POST.dict())
        # Here you can perform additional data validation if required
        # Create or update Evaluation object based on the validated data
        # Example:
        evaluation = Evaluations(
            StudentID_id=evaluation_data.student_id,
            EvaluatorID_id=evaluation_data.evaluator_id,
            EvaluationID=evaluation_data.evaluation_id,
            PaperID_id=evaluation_data.paper_id,
            Marks=evaluation_data.marks,
            UploadTime=evaluation_data.upload_time,
            Student_Rating=evaluation_data.student_rating,
            Evaluator_Rating=evaluation_data.evaluator_rating
        )
        evaluation.save()
        return JsonResponse({"message": "Answer evaluated successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})

@require_POST
def provide_feedback(request):
    if request.method == 'POST':
        feedback_data = FeedbackRequest(**request.POST.dict())
        # Here you can perform additional data validation if required
        # Create or update Evaluated_Questions object based on the validated data
        # Example:
        evaluated_question = Evaluated_Questions(
            EvaluationID_id=feedback_data.evaluation_id,
            QP_ID_id=feedback_data.qp_id,
            GroupMarks_id=feedback_data.group_marks,
            QuestionNumber=feedback_data.question_number,
            Marks=feedback_data.marks,
            Feedback=feedback_data.feedback
        )
        evaluated_question.save()
        return JsonResponse({"message": "Feedback provided successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})
