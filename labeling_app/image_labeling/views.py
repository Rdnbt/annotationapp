from django.shortcuts import redirect, render
from .models import ImageAnnotation

def label_image(request):
    # Retrieve random image annotation from the database
    image_annotation = ImageAnnotation.objects.order_by('?').first()
    image_path = image_annotation.image_path
    
    # Pass the image path to the template 
    context = {'iamge_path':image_path}

    # Render the template with the image path 
    return render(request, 'label_image.html', context)

def submit_annotation(request):
    if request.method == 'POST':
        annotation = request.POST['annotation']
        
        # Save the annotation to the database or file
        # Here, you can create a new ImageAnnotation object and save it
        image_annotation = ImageAnnotation.objects.create(
            image_path=request.POST['image_path'],
            annotation=annotation
        )
        
        # Redirect to the next image labeling page
        return redirect('label_image')
 