from tours.data import departures, title


def base_html(request):
    return {'departures': departures, 'title': title}
