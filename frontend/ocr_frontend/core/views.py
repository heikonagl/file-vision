import requests
from django.shortcuts import render
from django.http import HttpResponse

FASTAPI_URL = "http://localhost:8000"


def index(request):
    return render(request, "core/index.html")


def upload_image(request):
    if request.method == "POST":
        uploaded_file = request.FILES["imagefile"]
        files = {"file": uploaded_file.read()}
        # OCR-Anfrage an FastAPI
        response = requests.post(f"{FASTAPI_URL}/ocr", files=files)
        data = response.json()
        extracted_text = data.get("extracted_text", "")
        return render(request, "core/result.html", {"text": extracted_text})
    return HttpResponse("Method not allowed", status=405)
