from django.db import models

class PictureModel(models.Model):
    title = models.CharField(max_length=200)
    picture1 = models.CharField(max_length=200)
    picture2 = models.CharField(max_length=200, null=True, blank=True)
    picture3 = models.CharField(max_length=200, null=True, blank=True)
    picture4 = models.CharField(max_length=200, null=True, blank=True)
    picture5 = models.CharField(max_length=200, null=True, blank=True)
    picture6 = models.CharField(max_length=200, null=True, blank=True)
    discription = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title