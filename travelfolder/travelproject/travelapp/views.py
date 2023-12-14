from django.http import HttpResponse
from django.shortcuts import render

from travelapp.models import Place, Person


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj1 = Person.objects.all()
    return render(request, "index.html", {'result': obj, 'results': obj1})
