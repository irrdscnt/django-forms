from django.db import models

class Serie(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='')
    date=models.TextField(null=True)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    date=models.TextField(null=True)

    def __str__(self):
        return self.title