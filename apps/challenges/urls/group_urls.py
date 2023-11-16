from django.urls import path

from .. import views

app_name = "groups"
urlpatterns = [
    path(
        "<int:pk>/",
        views.ChallengeGroupDetailView.as_view(),
        name="group-detail",
    ),
    path(
        "<int:pk>/update/",
        views.ChallengeGroupUpdateView.as_view(),
        name="group-update",
    ),
    path(
        "create/",
        views.ChallengeGroupCreateView.as_view(),
        name="group-create",
    ),
    path(
        "<int:pk>/add/",
        views.FavoriteGroupAddView.as_view(),
        name="favorite-add",
    ),
    path(
        "<int:pk>/remove/",
        views.FavoriteGroupRemoveView.as_view(),
        name="favorite-remove",
    ),
]
