from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "<int:common_area_id>/common_area/",
        view=views.common_area,
        name="common_area"
    ),
    path(
        "<int:habitational_area_id>/habitational_area/",
        view=views.habitational_area,
        name="habitational_area"
    ),
]