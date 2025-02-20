from django.conf import settings
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'backoffice/index.html', {
        'debug': settings.DEBUG
    })
