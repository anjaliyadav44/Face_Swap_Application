from django import forms

class UploadImageForm(forms.Form):
    image1 = forms.ImageField()
    image2 = forms.ImageField()
