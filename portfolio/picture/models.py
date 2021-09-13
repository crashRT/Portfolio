from django.db import models

class PictureModel(models.Model):
    picture = models.ImageField(upload_to='pictures/')
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.title