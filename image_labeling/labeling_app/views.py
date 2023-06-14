import random
import os 
import csv
from django.shortcuts import render
from django.conf import settings

def label_image(request):
    # Read the captions from the CSV file
    with open('/Users/erdenebat/Projects/annotationapp/image_labeling/data/output_1000.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        image_captions = list(reader)

   # Randomly select an image and its caption
    image_caption = random.choice(image_captions)
    image_filename = image_caption[0]
    caption = image_caption[2]

    # Update the image path
    image_path = os.path.join(settings.STATIC_URL, 'flickr1000', image_filename)
    
    if request.method == 'POST':
        annotation = request.POST.get('annotation')
        print(annotation)  # Print the annotation to the console

    # Pass the image path and caption to the template
    context = {'image_path': image_path, 'caption': caption}

    return render(request, 'label_image.html', context) 