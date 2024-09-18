import os
import django

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  # Replace 'your_project_name' with the actual project name
django.setup()

from foodie.models import Restaurant

def print_list():
    for i in Restaurant.objects.all():
        print(i)

def add_img_urls():
    image_urls = ['varsity', 'vortex_grill', 'ecco', 'fresh_to_order', 'cypress', 'j_christopher', 'taco_mac',
                  'hudson_grille', 'papa_johns', 'shakespeare', 'marlows_tavern', 'publik', 'silver_skillet',
                  'rocky_mountain', 'livingston', 'apache', 'rays', 'optimist', 'steamhouse', 'dominos', 'thumbs_up',
                  'starbucks', 'der_biergarten', 'melting_pot', 'pizza_hut', 'babs', 'tabla', 'firehouse', 'jimmy_johns',
                  'mellow_mushroom', 'lucky_buddha', 'waffle_house', 'auto_spa', 'cafe_intermezzo', 'satto', 'gios',
                  'five_guys', 'jimmy_johns_2', 'edgars', 'papis', '11th', 'wingnuts', 'moes', 'jimmy_johns_2',
                  'tin_lizzys', 'crazy_cuban', 'vinnys', 'panda_express', 'tin_drum', 'tiff_treats', 'tropical',
                  'taco_bell', 'atwoods', 'gathering', 'pho_king', 'which_wich']

    for i in range(len(image_urls)):
        image_urls[i] = 'restaurant_images/' + image_urls[i] + '.jpg'

    print(image_urls)

    for i in range(len(image_urls)):
        restaurant = Restaurant.objects.all()[i]
        print(restaurant)
        restaurant.image = image_urls[i]
        print(restaurant.image)
        restaurant.save()

print_list()

add_img_urls()


