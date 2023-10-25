from django.shortcuts import render

# Create your views here.


def index(request):

    context = {'nav': 'index'}
    return render(request, 'index.html', context)


def about(request):
    context = {'nav': 'about'}
    return render(request, 'about.html', context)


def contact(request):
    context = {'nav': 'contact'}
    return render(request, 'contact.html', context)


def statistics(request):
    context = {'nav': 'statistics'}
    return render(request, 'statistics.html', context)


def loginform(request):
    context = {'nav': 'login'}
    return render(request, 'login.html', context)
