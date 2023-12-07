from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


def main_view(request):
    return render(request, template_name='tours/index.html')


def departure_view(request, departure):
    return render(request, template_name='tours/departure.html')


def tour_view(request, tour_id):
    return render(request, template_name='tours/tour.html')


def custom_404(request, exception):
    print(request)
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')


def custom_500(request):
    return HttpResponseServerError('Ой, что то сломалось... Простите извините!')
