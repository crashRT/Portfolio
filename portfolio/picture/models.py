from django.db import models

class PictureModel(models.Model):
    title = models.CharField(max_length=200)
    picture1 = models.ImageField(upload_to='picture', null = True, blank = True, default = '')
    picture2 = models.ImageField(upload_to='picture', null = True, blank = True, default = '')
    picture3 = models.ImageField(upload_to='picture', null = True, blank = True, default = '')
    picture4 = models.ImageField(upload_to='picture', null = True, blank = True, default = '')
    picture5 = models.ImageField(upload_to='picture', null = True, blank = True, default = '')
    picture6 = models.ImageField(upload_to='picture', null = True, blank = True, default = '')
    discription = models.CharField(max_length=1000)

    def __str__(self):
        return self.title