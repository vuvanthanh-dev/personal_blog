from django.urls import path

from . import views

app_name = "post"
urlpatterns = [
    path("", views.get_all_posts, name="get_all_posts"),
    path("get-by-id/<str:id>", views.get_post_by_id, name="get_post_by_id"),
    path("get-by-slug/<str:slug>", views.get_post_by_slug, name="get_post_by_slug"),
    path("get-by-tag/<str:tag_slug>", views.get_post_by_tag, name="get_post_by_tag"),
    path("get-by-category/<str:category_slug>", views.get_post_by_category, name="get_post_by_category"),
]
