from django.shortcuts import render
from .forms import ImageUploadForm
from PIL import Image
import pytesseract


def home(request):
    return render(request, "core/home.html")


def upload_image(request):
    extracted_text = None
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            # Optional: Speichern des Bildes
            # uploaded_image = UploadedImage.objects.create(image=image)

            # OCR-Verarbeitung
            img = Image.open(image)
            extracted_text = pytesseract.image_to_string(
                img, lang="de"
            )  # Sprache auf Deutsch setzen

    else:
        form = ImageUploadForm()

    return render(
        request, "ocr_app/upload.html", {"form": form, "extracted_text": extracted_text}
    )
