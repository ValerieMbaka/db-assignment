from django.db import models

# Create your models here.
class User(models.Model):
        username = models.CharField(max_length=100, blank=False, null=False)
        email = models.EmailField(max_length=100, blank=False, null=False)

        def __str__(self):
                return self.username