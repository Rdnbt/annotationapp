from django.db import models

class ImageAnnotation(models.Model):
    image_path = models.CharField(max_length=255)
    annotation = models.TextField()

    def __str__(self):
        return self.image_path
