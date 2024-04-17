from django.db import models

# Create your models here.
class Prep(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    num= models.IntegerField()

    def __str__(self):
        return self.name
