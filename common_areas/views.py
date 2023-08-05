from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from datetime import date, timedelta, datetime
from .forms import CommonAreaReservationForm

from .models import (
    Common_Area,
    Person,
    Location,
    Habitational_Area,
    Home,
    CommonAreaReservation
)

_FORM_DATE_FORMAT = "%Y-%m-%d"

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
    today = date.today().strftime(_FORM_DATE_FORMAT) 
    one_year = (datetime.utcnow() + timedelta(days=365)).strftime(_FORM_DATE_FORMAT)
    context.update({"today": today, "one_year_in_future": one_year})
    return render(
        request=request,
        template_name="common_areas/common_area.html",
        context=context
    )

def reserve_common_area(request):
    if request.method == "POST":
        form_result = CommonAreaReservationForm(request.POST)
        if form_result.is_valid():
            reservation_date = form_result.cleaned_data['reservation_date']
            confirmation_email = form_result.cleaned_data['confirmation_email']
            import pdb; pdb.set_trace()
    else:
        reservation_form = CommonAreaReservationForm()
        # import pdb; pdb.set_trace()
        today = date.today().strftime(_FORM_DATE_FORMAT)
        one_year = (datetime.utcnow() + timedelta(days=365)).strftime(_FORM_DATE_FORMAT)
        context = {"min": today}
        context.update({ "max": one_year})
        context.update({"reservation_form": reservation_form})
        return render(
            request, 
            "common_areas/reserve_common_area.html", 
            context
        )