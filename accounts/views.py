from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, FormView, DetailView
from accounts.forms import UserCreationForm, UserProfileUpdateForm, SignUpForm
from accounts.models import Profile


class SubmittableloginView(LoginView):
    template_name = "forms/form.html"


class SignUpView(CreateView):
    template_name = "forms/form.html"
    form_class = SignUpForm
    success_url = reverse_lazy("hello")


class SubmittablePasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "forms/form.html"
    success_url = reverse_lazy("hello")


class ProfileDetailedView(DetailView):
    template_name = "profile_detailed_view.html"
    model = Profile


class ProfileUpdateView(UpdateView):
    template_name = 'forms/form.html'
    form_class = UserProfileUpdateForm
    model = Profile
    success_url = reverse_lazy('hello')
