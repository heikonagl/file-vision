from django import forms


class ImageUploadForm(forms.Form):
    image = forms.ImageField(label="Wähle ein Bild")
