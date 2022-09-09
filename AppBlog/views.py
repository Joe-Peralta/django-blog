from django.shortcuts import render, HttpResponse

# Create your views here.


def Blog(request):
    return HttpResponse('Pagina de Blog')