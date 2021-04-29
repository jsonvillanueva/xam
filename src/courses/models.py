from django.db import models
from django.urls import reverse


class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("courses:course-detail", kwargs={"id": self.id})
