from django.shortcuts import render
from django.db import models
from .models import Item


def home(request):
    a = []
    for x in Item.objects.all():
        a.append(x)

    content = {
        'items': a,
    }

    return render(request, 'home.html', content)

