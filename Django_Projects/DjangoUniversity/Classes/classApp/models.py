from django.db import models

# Create your models here.
class djangoClass(models.Model):
    Title = models.CharField(max_length=60, default="", blank=True)
    CourseNumber = models.IntegerField(default="", blank=True, null=False)
    Instructor = models.CharField(max_length=60, default="", blank=True)
    Duration = models.FloatField(default=0.0, blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.Title
