from django.http import HttpResponse


def index(request):
    return HttpResponse('OK index')


def login(request):
    return HttpResponse('OK login')


def signup(request):
    return HttpResponse('OK signup')


def question(request, id):
    return HttpResponse('OK question=' + id)


def ask(request):
    return HttpResponse('OK ask')


def popular(request):
    return HttpResponse('OK popular')


def new(request):
    return HttpResponse('OK new')
