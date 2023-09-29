from django.http import HttpResponse


def dip2(request):
    return HttpResponse("Hello This is from Dip2 ( WinHtut)app")

def home(request):
    return HttpResponse("This is from home page winhtut app!")
# Create your views here.
