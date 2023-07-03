from django.shortcuts import render, HttpResponse

from .models import Common_Area, Person, Location, Habitational_Area, Home

# Create your views here.
def index(request):
    return HttpResponse("Hello, this is commoan areas running")


def common_area(request, common_area_id):
    _ = f"Ready to see a common area: {common_area_id}"
    return HttpResponse(_)