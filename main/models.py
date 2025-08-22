from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class MediaFiles(models.Model):
    MEDIA_TYPES = [
        ('movie', 'Movie'),
        ('music', 'Music'),
        ('photos', 'Photos')
    ]

    title = models.CharField(max_length=192)
    file = models.FileField(upload_to='media/')
    thumbnail = models.ImageField(upload_to='media/', blank=True, null=True)

    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    duration = models.CharField(max_length=20, blank=True, null=True)
    size = models.PositiveIntegerField(blank=True, null=True)

    folder = models.ForeignKey(Folder, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title