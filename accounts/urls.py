from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import SubmittableloginView, SignUpView, SubmittablePasswordChangeView, ProfileDetailedView, \
    ProfileUpdateView

app_name = "accounts"




urlpatterns = [
    path("login/", SubmittableloginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("sign-up/", SignUpView.as_view(), name="sign_up"),
    path("password-change/", SubmittablePasswordChangeView.as_view(), name="password_change"),
    path("profile/<int:pk>/", ProfileDetailedView.as_view(), name="profile_view"),
    path("profile/<int:pk>/update/", ProfileUpdateView.as_view(), name="profile_update"),
]
