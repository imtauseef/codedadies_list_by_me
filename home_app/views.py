from typing import Text
import requests
from urllib.parse import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Search

# Create your views here.
BASE_CRAIGSLIST_URL = "https://newyork.craigslist.org/d/services/search/bbb?query={}"
BASE_IMAGE_URL = "https://images.craigslist.org/{}_300x300.jpg"

def home(request):
    return render(request, template_name="base.html")


def search(request):
    searched_things = request.POST.get('search')
    Search.objects.create(search_field=searched_things)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(searched_things))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})

    final_postings = []
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = "N/A"

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
        else:
            post_image_url = "https://craigslist.org/images/peace.jpg"
    
        final_postings.append((post_title, post_url, post_price, post_image_url))

    context = {
        'searched_things': searched_things,
        'final_postings': final_postings,
    }

    return render(request, "home_app/search.html", context)