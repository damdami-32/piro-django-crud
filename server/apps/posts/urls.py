from django.urls import path

from server.apps.posts.views import posts_list, posts_create, posts_retrieve, posts_update, posts_delete
urlpatterns = [
    path("", posts_list),
    path("posts/create", posts_create),
    path("posts/<int:pk>", posts_retrieve),
    path("posts/<int:pk>/update", posts_update),
    path("posts/<int:pk>/delete", posts_delete),
]