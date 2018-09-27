from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=48)
    rated = models.CharField(max_length=48)
    relased = models.CharField(max_length=48)
    runtime = models.CharField(max_length=48)
    genre = models.CharField(max_length=48)
    plot = models.CharField(max_length=250)
    language = models.CharField(max_length=48)

    def __str__(self):
        return self.title


class Comments(models.Model):
    text = models.CharField(max_length=250)
    movies = models.ForeignKey(Movies, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
