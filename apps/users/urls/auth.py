from django.urls import include, path

from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
