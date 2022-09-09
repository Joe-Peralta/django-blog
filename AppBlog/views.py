from django.shortcuts import render, HttpResponse

# Create your views here.


def Blogs(request):
    return HttpResponse('<h1> Pagina de Blogs </h1>')

def Blog(request,id):
    return HttpResponse('<h1> Blog </h1>')