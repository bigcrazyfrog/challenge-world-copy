from django.urls import path

from .. import views

app_name = "challenges"
urlpatterns = [
    path(
        "",
        views.ChallengeListView.as_view(),
        name="challenge-list",
    ),
    path(
        "<int:pk>/",
        views.ChallengeDetailView.as_view(),
        name="challenge-detail",
    ),
    path(
        "create/",
        views.ChallengeCreateView.as_view(),
        name="challenge-create",
    ),
    path(
        "complete/",
        views.ChallengeCompleteView.as_view(),
        name="challenge-complete",
    ),
]
