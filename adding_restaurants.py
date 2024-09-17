from django.utils.archive import extract

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from foodie.models import Restaurant
from foodie.localSettings import MAPS_API_KEY

import requests
import time

def extract_restaurants(location):
    radius = 1500
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&type=restaurant&radius={radius}&key={MAPS_API_KEY}'
    pages = 0

    while pages < 5:
        response = requests.get(url)
        places = response.json()

        restaurants_list = places['results']
        for restaurant in restaurants_list:
            place_id = restaurant['place_id']
            details_url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={MAPS_API_KEY}'
            response = requests.get(details_url)
            details = response.json()
            details = details['result']

            restaurant_object = Restaurant(name=details['name'], cuisine="TEMP - CHANGE THIS !", address=details['formatted_address'], street=details["address_components"][1]['long_name'], zip_code=details["address_components"][-1]['long_name'], longitude=details['geometry']['location']['lng'], latitude=details['geometry']['location']['lat'], phone_number=details.get("formatted_phone_number", None), website=details.get("website", None), overall_rating=details["rating"], reviews=details["reviews"])
            restaurant_object.save()

        pages += 1

        next_page_token = places.get('next_page_token')
        if next_page_token:
            time.sleep(2)
            url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={next_page_token}&key={MAPS_API_KEY}'
        else:
            break

def print_restaurants():
    for restaurant in Restaurant.objects.all():
        print(restaurant)

def delete_all():
    Restaurant.objects.all().delete()

def add_cuisine():
    restaurant_list = Restaurant.objects.all()
    cuisine_list = ['American', 'American', 'European', 'American', 'American', 'American', 'American', 'American',
                    'Italian', 'British', 'American', 'American', 'Greek', 'Southern', 'Italian', 'Southern', 'Southern',
                    'Cafe', 'Italian', 'Seafood', 'Seafood', 'Italian', 'American', 'Cafe', 'German', 'French',
                    'Italian', 'American', 'Indian', 'American', 'American', 'Italian', 'Chinese', 'American Breakfast',
                    'American', 'European', 'Asian', 'Italian', 'American', 'American', 'American', 'Cuban', 'American',
                    'American', 'Mexican', 'American', 'Tex Mex', 'Cuban', 'Italian', 'DELETE', 'American', 'Chinese',
                    'Asian', 'Desert', 'Cafe', 'Mexican', 'Italian', 'American', 'Vietnamese', 'American']

    #print(len(cuisine_list))
    for i in range(len(restaurant_list)):
        restaurant_list[i].cuisine = cuisine_list[i]
        restaurant_list[i].save()

if __name__ == "__main__":
    # extract_restaurants('33.7752903739364, -84.39628605801305')
    #print_restaurants()
    add_cuisine()