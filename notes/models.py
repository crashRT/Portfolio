from django.db import models

# Create your models here.

CATEGORY = (('3dcg', '3dcg'),
            ('web', 'web'),
            ('linux', 'linux'),
            ('other', 'other')
            )

tags = ('3dcg', 'web', 'Linux')


class NotesModel(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    abstract = models.TextField()
    url = models.TextField()
    tag = models.CharField(
        max_length=30, choices=CATEGORY, null=True, blank=True)

    def __str__(self):
        return self.title
