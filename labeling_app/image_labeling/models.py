from django.db import models

# Defines ImageAnnotation model with two fields: 'image_path' and 'annotation'
# The image_path field is a CharField that stores the path of the image file, and the annotation field is a TextField that stores the Mongolian annotation text.

from django.db import models

class ImageAnnotation(models.Model):
    image_path = models.CharField(max_length=255)
    annotation = models.TextField()

    def __str__(self):
        return self.image_path

    def get_image_url(self):
        return f'http://localhost:3000/{self.image_path}'
