from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Hello OCR!"}


# @app.post("/ocr")
# async def ocr_endpoint(file: UploadFile = File(...)):
#     # Lade das übertragene Bild in PIL
#     image_bytes = await file.read()
#     image = Image.open(io.BytesIO(image_bytes))

#     # OCR mit pytesseract
#     text = pytesseract.image_to_string(image)

#     return {"extracted_text": text}
