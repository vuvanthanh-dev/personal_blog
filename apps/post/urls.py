from django.urls import path

from . import views

app_name = "post"
urlpatterns = [
    path("", views.get_all_posts, name="get_all_posts"),
    path("<str:slug>", views.get_post_by_slug, name="get_post_by_slug"),
    path("tag/<str:tag_slug>", views.get_post_by_tag, name="get_post_by_tag"),
    path("category/<str:category_slug>", views.get_post_by_category, name="get_post_by_category"),
]
