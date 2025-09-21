from django.shortcuts import render, HttpResponse
import random
import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()


def main(request):
    c = int(request.GET.get('c', random.randint(0, 18)))
    page = int(request.GET.get('page', 1) or c)

    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": getenv('TMDB_API')
    }

    response = requests.get(url, headers=headers).json()

    q = 0

    picture = (response['results'][c]['poster_path'])
    title = (response['results'][c]['title'])
    desc = (response['results'][c]['overview'])

    context = {'title': title,
               'picture': f'https://image.tmdb.org/t/p/w300/{picture}', 'desc': desc, 'c': c}
    submitbutton = request.POST.get('Submit')

    if submitbutton:
        while c < len(response['results']):
            if c > len(response['results']):
                c = 0
                page += 1
            else:
                c += 1
    return render(request, 'popular_film.html', context)


def top_rated(request):
    page = int(request.GET.get('page', 1))

    url = f"https://api.themoviedb.org/3/tv/top_rated?language=en-US&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": getenv('TMDB_API')
    }

    response = requests.get(url, headers=headers).json()
    context = {
        'res': [
            {
                'title': movie.get('title') or movie.get('original_name'),
                'picture': f"https://image.tmdb.org/t/p/w300/{movie['poster_path']}",
                'desc': movie.get('overview'),
                'rate': ("%.1f" % movie.get('vote_average'))
            }
            for movie in response['results']
        ],
        'page': page  # передаём отдельно, вне списка фильмов
    }

    submitbutton = request.POST.get('Submit')
    if submitbutton:
        page += 1

    return render(request, 'top_rated.html', context)
