from django.db import models

# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Organizaytion(models.Model):
    name = models.CharField(max_length=50)
    deskription = models.TextField()
    since = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Building(models.Model):
    organization = models.ForeignKey(Organizaytion, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    field = models.IntegerField()
    floor = models.IntegerField()
    parkovka = models.BooleanField()
    playground = models.BooleanField()
    lift = models.BooleanField()

    def __str__(self):
        return self.name

