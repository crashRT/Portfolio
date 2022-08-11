from django.db import models

# Create your models here.

CATEGORY = (('pictre', 'Picture'),
            ('movie', 'Movie'),
            ('modeling', 'Modeling'),
            ('other', 'other')
            )


class WorksModel(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.TextField()
    youtube = models.TextField(null=True, blank=True)
    vimeo = models.TextField(null=True, blank=True)
    niconico = models.TextField(null=True, blank=True)
    picture1 = models.TextField(null=True, blank=True)
    picture2 = models.TextField(null=True, blank=True)
    picture3 = models.TextField(null=True, blank=True)
    picture4 = models.TextField(null=True, blank=True)
    picture5 = models.TextField(null=True, blank=True)
    picture6 = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tag = models.CharField(max_length=30, choices=CATEGORY)
