from django.db import models

# Create your models here.

CATEGORY = (('pictre', 'Picture'),
            ('movie', 'Movie'),
            ('modeling', 'Modeling'),
            ('other', 'other')
            )


class WorksModel(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.CharField(max_length=100,)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    vimeo = models.CharField(max_length=100, null=True, blank=True)
    niconico = models.CharField(max_length=100, null=True, blank=True)
    pictureMain = models.CharField(max_length=100, null=True, blank=True)
    picture1 = models.CharField(max_length=100, null=True, blank=True)
    picture2 = models.CharField(max_length=100, null=True, blank=True)
    picture3 = models.CharField(max_length=100, null=True, blank=True)
    picture4 = models.CharField(max_length=100, null=True, blank=True)
    picture5 = models.CharField(max_length=100, null=True, blank=True)
    picture6 = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tag = models.CharField(max_length=30, choices=CATEGORY)

    def __str__(self):
        return self.title
