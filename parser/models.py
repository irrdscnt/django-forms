from django.db import models

class Laptop(models.Model):
    title = models.CharField(max_length=100)
    title_text=models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=6)
    image = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title
