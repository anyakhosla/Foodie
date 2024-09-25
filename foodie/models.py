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
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(max_length=300, null=True, blank=True)

    # ratings and reviews
    overall_rating = models.FloatField()
    reviews = models.JSONField(default=list, blank=True)

    image = models.ImageField(upload_to='restaurant_images/', null=True, blank=True)


    def __str__(self):
        return f"{self.name}"

class User(models.Model):
    name = models.CharField(max_length=200)

    # address info
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    favorite_restaurants = models.ManyToManyField(Restaurant, related_name='favorited_by', blank=True) # restaurants can get people that favorited them with the related_name field
    # many to many should automatically handle deletions of a favorite restaurant when that restaurant is deleted


    # contact info
    phone_number = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
