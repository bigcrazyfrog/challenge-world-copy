from django.urls import path

from .. import views

app_name = "users"
urlpatterns = [
    path(
        "<str:username>/",
        views.ProfileView.as_view(),
        name="detail",
    ),
    path(
        "profile/edit/",
        views.ProfileEditView.as_view(),
        name="edit",
    ),
]
