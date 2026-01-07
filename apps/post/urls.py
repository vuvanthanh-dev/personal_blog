from django.urls import path

from . import views

app_name = "post"
urlpatterns = [
    path("", views.get_all_posts, name="get_all_posts"),
    path("<str:slug>", views.get_post_by_slug, name="get_post_by_slug"),
]
