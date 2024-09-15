from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=20)

    # address info
    address = models.CharField(max_length=200)
    street = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    # we aren't breaking out any of the other address values because all the restaurants are in Atlanta and therefore
    # are in the same city, country, etc
    longitude = models.FloatField()
    latitude = models.FloatField()

    # contact info
    phone_number = models.CharField(max_length=15)
    website = models.CharField(max_length=300)

    # ratings and reviews
    overall_rating = models.FloatField()
    reviews = models.JSONField(default=list, blank=True)