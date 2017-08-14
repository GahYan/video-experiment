from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
class Video(models.Model):
    #tags=models.ListCharField(CharField, size=None, **kwargs)
    name=models.CharField(max_length=200)
    link=models.TextField()
    tags=TaggableManager()
    def __str__(self):              # __unicode__ on Python 2
        return self.name
