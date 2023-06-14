from django.shortcuts import render
from .models import ImageAnnotation

def label_image(request):
    # Retrieve a random image annotation from the database
    image_annotation = ImageAnnotation.objects.order_by('?').first()
    image_path = image_annotation.image_path

    # Pass the image path to the template
    context = {'image_path': image_path}

    # Render the template with the image path
    return render(request, 'label_image.html', context)
