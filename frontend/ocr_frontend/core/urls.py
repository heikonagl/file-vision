from django.urls import path
from .views import index, upload_image

urlpatterns = [
    path("", index, name="index"),
    path("upload/", upload_image, name="upload_image"),
]
