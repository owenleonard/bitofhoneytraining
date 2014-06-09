from django.db import models

# Create your models here.
class Testimonial(models.Model):
    text = models.TextField()
    person = models.CharField(max_length=256)
    link = models.URLField(default=None, blank=True)
    display = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.person
