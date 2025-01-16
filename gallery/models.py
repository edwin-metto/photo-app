from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='photos/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    created_at = models.DateTimeField( default='2025-01-01')


    def __str__(self):
        return self.title
