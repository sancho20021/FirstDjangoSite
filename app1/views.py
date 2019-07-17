from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random


def index(request):

    if request.method == 'GET':
        a = ['Автомобиль', 'Шрека', 'Круассан', 'Поездку в ГоуТу', '']
        prize = random.choice(a)
        return render(request, 'index.html', {'prize': prize})
    return HttpResponse("aaa")