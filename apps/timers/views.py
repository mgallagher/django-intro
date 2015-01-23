from django.shortcuts import render

from .models import Timer


def home(request):
    timers = Timer.objects.all()
    return render(request, 'index.html', {'timers': timers})
