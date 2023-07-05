from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from .models import Common_Area, Person, Location, Habitational_Area, Home

# Create your views here.
def index(request):
    try:
        habitational_area = Habitational_Area.objects.get(id=1)
    except Habitational_Area.DoesNotExist as dne:
        raise Http404("Habitational Area not exits")
    common_areas = Common_Area.objects.filter(
            habitational_area=habitational_area
        ).order_by('id')[:10]
    context = {
        'habitational_area': habitational_area,
        'common_areas': common_areas
    }
    return render(request,"common_areas/index.html" ,context=context)


def habitational_area(request, habitational_area_id):
    try:
        ha = Habitational_Area.objects.get(pk=habitational_area_id)
        common_areas = Common_Area.objects.filter(habitational_area=ha)
        context = {
            'habitational_area': ha,
            'common_areas': common_areas
        }
    except Habitational_Area.DoesNotExist as hane:
        raise Http404("Habitational Area not exists")
    return render(
        request=request,
        template_name="common_areas/index.html",
        context=context
    )

def common_area(request, common_area_id):
    common_area = get_object_or_404(Common_Area, pk=common_area_id)
    print(common_area.name)
    context = {'common_area': common_area}
    return render(
        request=request,
        template_name="common_areas/common_area.html",
        context=context
    )