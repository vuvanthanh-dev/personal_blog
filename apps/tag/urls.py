from django.urls import path
from . import views


app_name = "tag"
urlpatterns = [
    path("", views.tag_list, name="tag_list"),
    path("<slug:slug>", views.tag_detail, name="tag_detail"),
    path("create/", views.create_tag, name="create_tag"),
    path("update/<slug:slug>", views.update_tag, name="update_tag"),
    path("delete/<slug:slug>", views.delete_tag, name="delete_tag")
]