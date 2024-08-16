from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi there! My name is Ali!")


def leo(request):
    return HttpResponse("Ты настоящий лев, вацок!")


def wolf(request):
    return HttpResponse("Ты настоящий волк, вацок!")