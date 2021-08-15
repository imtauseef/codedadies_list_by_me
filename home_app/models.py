from django.db import models

# Create your models here.
class Search(models.Model):
    search_field = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.search_field

    class Meta:
        verbose_name_plural = "Searches"