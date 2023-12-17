import random
import tours.data as data
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


def index_view(request):
    random_tours_index = random.sample(list(data.tours.keys()), 6)
    random_tours = {k: v for k, v in data.tours.items() if k in random_tours_index}
    context = {'tours': random_tours,
               'description': data.description,
               'subtitle': data.subtitle
               }
    return render(request, template_name='tours/index.html', context=context)


def departure_view(request, departure):
    tours = {k: v for (k, v) in data.tours.items() if v['departure'] == departure}
    prices = [i['price'] for i in tours.values()]
    nights = [i['nights'] for i in tours.values()]
    context = {
        'tours': tours,
        'departure_from': data.departures.get(departure),
        'max_price': max(prices),
        'min_price': min(prices),
        'min_nights': min(nights),
        'max_nights': max(nights)
    }
    return render(request, template_name='tours/departure.html', context=context)


def tour_view(request, tour_id):
    tour = data.tours.get(tour_id, 'Такого тура не существует')
    context = {
        'tour': tour,
        'departure_from': data.departures.get(data.tours.get(tour_id).get('departure'))
    }
    return render(request, template_name='tours/tour.html', context=context)


def custom_404(request, exception):
    print(request)
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def custom_500(request):
    return HttpResponseServerError('Ой, что то сломалось... Простите извините!')
