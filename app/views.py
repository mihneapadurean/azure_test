from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .domain import Person

# Create your views here.
def home(request):
    return HttpResponse('Hello, world!')

def person_info(request, pk):
    try:
        person = Person.objects.get(pk=pk)
        return HttpResponse('\n'.join([person.first_name, person.last_name]))
    except Person.DoesNotExist:
        return HttpResponseNotFound("Not found")
