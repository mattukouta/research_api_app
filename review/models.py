from django.db import models


class Review(models.Model):
    sentence = models.TextField()
    hotel = models.CharField(max_length=20)
    purpose = models.CharField(max_length=20)
    companion = models.CharField(max_length=20)


class Hotel(models.Model):
    HotelID = models.CharField(max_length=20)
    Prefectures = models.CharField(max_length=20)
    Cities = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
