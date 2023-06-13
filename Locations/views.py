from django.shortcuts import render

# Create your views here.


from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Beautiful
from rest_framework import generics
from . import serializer



# получение данных из бд
def index(request):
    location = Beautiful.objects.all()
    return render(request, "index1.html", {"location": location})



# сохранение данных в бд
def create(request):
    if request.method == "POST":
        locations = Beautiful()
        locations.city = request.POST.get("city")
        locations.country = request.POST.get("country")
        locations.date = request.POST.get("date")
        locations.save()
    return HttpResponseRedirect("/Locations")


# изменение данных в бд
def edit(request, id):
    try:
        locations = Beautiful.objects.get(id=id)

        if request.method == "POST":
            locations.city = request.POST.get("city")
            locations.country = request.POST.get("country")
            locations.date = request.POST.get("date")
            locations.save()
            return HttpResponseRedirect("/Locations")
        else:
            return render(request, "edit.html", {"locations": locations})
    except Beautiful.DoesNotExist:
        return HttpResponseNotFound("<h2>Locations not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        locations = Beautiful.objects.get(id=id)
        locations.delete()
        return HttpResponseRedirect("/Locations")
    except Beautiful.DoesNotExist:
        return HttpResponseNotFound("<h2>Locations not found</h2>")


class BeautifulList(generics.ListAPIView):
    location = Beautiful.objects.all()
    serializer_class = serializer.BeautifulSerializer