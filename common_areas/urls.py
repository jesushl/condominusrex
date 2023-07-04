from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:common_area_id>", views.common_area, name="common_area")
]