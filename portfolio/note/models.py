from django.db import models

# Create your models here.
class NoteModel(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    abstract = models.CharField(max_length=200, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title