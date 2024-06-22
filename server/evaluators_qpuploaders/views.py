from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from .models import QP_Uploader, Evaluator, Eval_Languages, Eval_Subjects, Eval_Boards, Question_Papers, QP_Structure
from pydantic import BaseModel
from typing import List

# Pydantic models for data validation
class EvaluatorCreationRequest(BaseModel):
    name: str
    email: str
    password: str
    phone: str

class QPUploaderCreationRequest(BaseModel):
    name: str
    email: str
    password: str
    phone: str

class QuestionPaperCreationRequest(BaseModel):
    name: str
    uploader_id: int
    upload_date: str
    subject: str
    language: str
    board: str
    grade: int

class QPStructureCreationRequest(BaseModel):
    qp_id: int
    group_marks: int
    group_size: int

class QuestionPaperUploadRequest(BaseModel):
    uploader_id: int
    upload_date: str
    subject: str
    language: str
    board: str
    grade: int


@require_POST
def create_evaluator(request):
    if request.method == 'POST':
        evaluator_data = EvaluatorCreationRequest(**request.POST.dict())
        # Perform additional data validation if required
        evaluator = Evaluator(
            Name=evaluator_data.name,
            Email=evaluator_data.email,
            Password=evaluator_data.password,
            Phone=evaluator_data.phone,
            Rating=0  # Default rating
        )
        evaluator.save()
        return JsonResponse({"message": "Evaluator created successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})

@require_POST
def create_qp_uploader(request):
    if request.method == 'POST':
        uploader_data = QPUploaderCreationRequest(**request.POST.dict())
        # Perform additional data validation if required
        uploader = QP_Uploader(
            Name=uploader_data.name,
            Email=uploader_data.email,
            Password=uploader_data.password,
            Phone=uploader_data.phone
        )
        uploader.save()
        return JsonResponse({"message": "QP Uploader created successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})

@require_POST
def create_question_paper(request):
    if request.method == 'POST':
        paper_data = QuestionPaperCreationRequest(**request.POST.dict())
        # Perform additional data validation if required
        paper = Question_Papers(
            QP_Name=paper_data.name,
            QP_UploaderID_id=paper_data.uploader_id,
            QP_UploadDate=paper_data.upload_date,
            QP_Subject=paper_data.subject,
            QP_Language=paper_data.language,
            QP_Board=paper_data.board,
            QP_Grade=paper_data.grade
        )
        paper.save()
        return JsonResponse({"message": "Question Paper created successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})

@require_POST
def create_qp_structure(request):
    if request.method == 'POST':
        structure_data = QPStructureCreationRequest(**request.POST.dict())
        # Perform additional data validation if required
        structure = QP_Structure(
            QP_ID_id=structure_data.qp_id,
            Group_Marks=structure_data.group_marks,
            Group_Size=structure_data.group_size
        )
        structure.save()
        return JsonResponse({"message": "Question Paper Structure created successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})
