from django.shortcuts import render, HttpResponse

from .models import Common_Area, Person, Location, Habitational_Area, Home

# Create your views here.
def index(request):
    common_areas = Common_Area.objects.order_by('id')[:10]
    output = " ,".join([ca.name for ca in common_areas])
    return HttpResponse(output)


def common_area(request, common_area_id):
    _ = f"Ready to see a common area: {common_area_id}"
    return HttpResponse(_)