import random
import os 
import csv
from django.shortcuts import render
from django.conf import settings

# Note for myself - To keep track of the files on display - I need to modify the view.py and pass it to html file

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
        # Save the annotation to a CSV file
        save_annotation(image_filename, annotation)

        # Update the counter
        update_counter()

    # Get the current count from the counter file
    current_count = get_current_count()

    # Pass the image path, caption, and current count to the template
    context = {'image_path': image_path, 'caption': caption, 'current_count': current_count}

    return render(request, 'label_image.html', context)


def save_annotation(image_filename, annotation):
    # Define the path to the annotation CSV file
    annotation_file = os.path.join(settings.BASE_DIR, 'data', 'annotated', 'annotations.csv')

    # Check if the annotation file already exists
    file_exists = os.path.isfile(annotation_file)

    # Open the annotation file in append mode and write the annotation data
    with open(annotation_file, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')

        # Write the header row if the file doesn't exist
        if not file_exists:
            writer.writerow(['image_name', 'comment_number', 'comment'])

        # Determine the comment number based on the existing annotations
        comment_number = get_comment_number(annotation_file, image_filename)

        # Write the new annotation
        writer.writerow([image_filename, comment_number, annotation])


def get_comment_number(annotation_file, image_filename):
    # Read the existing annotations to determine the comment number
    with open(annotation_file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        rows = list(reader)

        # Find the maximum comment number for the current image filename
        comment_numbers = [int(row[1]) for row in rows if row[0] == image_filename]
        max_comment_number = max(comment_numbers) if comment_numbers else -1

        # Increment the maximum comment number to get the next available comment number
        comment_number = max_comment_number + 1

    return comment_number


def update_counter():
    # Define the path to the counter file
    counter_file = os.path.join(settings.BASE_DIR, 'data', 'counter.txt')

    # Read the current count from the counter file
    current_count = get_current_count()

    # Increment the count
    current_count += 1

    # Write the updated count to the counter file
    with open(counter_file, 'w') as file:
        file.write(str(current_count))


def get_current_count():
    # Define the path to the counter file
    counter_file = os.path.join(settings.BASE_DIR, 'data', 'counter.txt')

    # Read the current count from the counter file
    with open(counter_file, 'r') as file:
        current_count = int(file.read())

    return current_count