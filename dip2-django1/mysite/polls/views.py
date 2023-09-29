from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello this is first app from Django!")


def home(request):
    return HttpResponse("This is from home Page!Poll app")
# Create your views here.
