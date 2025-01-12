from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .forms import UploadImageForm
from .face_swap import swap_faces

def home(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image1 = request.FILES['image1']
            image2 = request.FILES['image2']

            image1_name = default_storage.save(image1.name, ContentFile(image1.read()))
            image2_name = default_storage.save(image2.name, ContentFile(image2.read()))

            output_path = 'swapper/static/swapper/output.jpg'

            swap_faces(default_storage.path(image1_name), default_storage.path(image2_name), output_path)

            return render(request, 'swapper/result.html', {'image': 'swapper/output.jpg'})
    else:
        form = UploadImageForm()
    return render(request, 'swapper/home.html', {'form': form})

