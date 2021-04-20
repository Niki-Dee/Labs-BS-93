from django.db import models


class Beer(models.Model):
    title = models.CharField("Name", max_length=50)
    components = models.CharField("Components", max_length=250)
    about = models.TextField("About Beer")
    date = models.DateTimeField("date of publication")

    def __str__(self):
        return self.title
# Create your models here.
