from django.db import models

# Create your models here.

CATEGORY = (('picture', 'Picture'),
            ('movie', 'Movie'),
            ('modeling', 'Modeling'),
            ('other', 'other')
            )

tags = ('picture', 'movie', 'modeling',)


class WorksModel(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(blank=True, null=True)
    thumbnail = models.CharField(max_length=100,)
    youtube = models.CharField(
        max_length=100, null=True, blank=True, help_text='youtubeのID')
    vimeo = models.CharField(max_length=100, null=True,
                                blank=True, help_text='vimeoのID')
    niconico = models.CharField(
        max_length=100, null=True, blank=True, help_text='niconicoのID')
    pictureMain = models.CharField(
        max_length=100, null=True, blank=True, help_text='一番上に単体で表示')
    picture1 = models.CharField(
        max_length=100, null=True, blank=True, help_text='以下はギャラリー部分')
    picture2 = models.CharField(max_length=100, null=True, blank=True)
    picture3 = models.CharField(max_length=100, null=True, blank=True)
    picture4 = models.CharField(max_length=100, null=True, blank=True)
    picture5 = models.CharField(max_length=100, null=True, blank=True)
    picture6 = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tag = models.CharField(max_length=30, choices=CATEGORY)

    def __str__(self):
        return self.title
