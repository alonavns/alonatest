from django.shortcuts import render

def index(request):
    context = {
        'title': 'Interview Cake Test',
    }
    return render(request, 'cakes/index.html', context)
