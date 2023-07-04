from django.shortcuts import render, HttpResponse

from .models import Common_Area, Person, Location, Habitational_Area, Home

# Create your views here.
def index(request):
    habitational_area = Habitational_Area.objects.get(id=1)
    common_areas = Common_Area.objects.filter(
            habitational_area=habitational_area
        ).order_by('id')[:10]
    context = {
        'habitational_area': habitational_area,
        'common_areas': common_areas
    }
    return render(request,"common_areas/index.html" ,context=context)


def common_area(request, common_area_id):
    _ = f"Ready to see a common area: {common_area_id}"
    return HttpResponse(_)