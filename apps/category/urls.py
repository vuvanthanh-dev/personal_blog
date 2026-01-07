from django.urls import path

from . import views


app_name = "category"
urlpatterns = [
    path("", views.get_all_categories, name="get_all_categories"),
    path("<str:slug>", views.get_category_by_slug, name="get_category_by_slug"),
]