from django.db import models
from django.urls import reverse

# Create your models here.

class person(models.Model):
    """Model representing an author."""

    record_id = models.CharField(max_length=20, default="", unique=True)
    x_nose = models.IntegerField(default="")
    y_nose = models.IntegerField(default="")
    x_shoulder = models.IntegerField(default="")
    y_shoulder = models.IntegerField(default="")

    # class Meta:
    #     ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('person-detail', args=[str(self.id)])

    # def __str__(self):
    #     """String for representing the Model object."""
    #     return f'{self.last_name}, {self.first_name}'


