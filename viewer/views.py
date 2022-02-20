from logging import getLogger

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from viewer.forms import MovieForm, GenreForm
from viewer.models import Movie, Genre

LOG = getLogger()


def search(request):
    title = request.GET.get("title")
    if title is None:
        return render(request, "search.html", context={"data": [], "count": 0})
    data = Movie.objects.filter(title__contains=title)
    return render(request, "search.html", context={"data": data, "count": data.count})


class StaffRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff


class Hello(TemplateView):
    template_name = "hello.html"


class Contact(TemplateView):
    template_name = "contact.html"


class MoviesView(ListView):
    template_name = "movies.html"
    model = Movie
    paginate_by = 5


class GenreListView(ListView):
    template_name = "genres.html"
    model = Genre


class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = "forms/form.html"
    form_class = MovieForm
    success_url = reverse_lazy("movies")
    permission_required = "viewer.add_movie"

    def form_invalid(self, form):
        LOG.warning("User provided invalid data.")
        return super().form_invalid(form)

    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     cleaned_data = form.cleaned_data
    #     Movie.objects.create(
    #         title=cleaned_data["title"],
    #         genre=cleaned_data["genre"],
    #         rating=cleaned_data["rating"],
    #         released=cleaned_data["released"],
    #         description=cleaned_data["description"],
    #     )
    #     return result


class MovieUpdateView(PermissionRequiredMixin, StaffRequiredMixin, UpdateView):
    template_name = 'forms/form.html'
    form_class = MovieForm
    model = Movie
    success_url = reverse_lazy('movies')
    permission_required = "viewer.change_movie"

    def form_invalid(self, form):
        LOG.warning("User provided invalid data while updating.")
        return super().form_invalid(form)


class MovieDeleteView(PermissionRequiredMixin, StaffRequiredMixin, DeleteView):
    template_name = 'forms/delete_movie_form.html'
    model = Movie
    success_url = reverse_lazy('movies')
    permission_required = "viewer.delete_movie"

    def test_func(self):
        return super().test_func() and self.request.user.is_superuser

    # def get(self, request, pk):
    #     if not Movie.objects.filter(id=pk).exists():
    #         return HttpResponse('Object does not exists.')
    #     return super().get(request)


class GenreCreateView(PermissionRequiredMixin, FormView):
    template_name = "forms/form.html"
    form_class = GenreForm
    success_url = reverse_lazy("create_genre")
    permission_required = 'viewer.add_genre'

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Genre.objects.create(
            name=cleaned_data["name"],
        )
        return result

    # def get(self, request):
    #     return render(request, 'movies.html', context={'movies': Movie.objects.all()})


class GenreUpdateView(StaffRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'forms/form.html'
    form_class = GenreForm
    model = Genre
    success_url = reverse_lazy('genres')
    permission_required = "viewer.change_genre"

    # def form_invalid(self, form):
    #     LOG.warning("User provided invalid data while updating.")
    #     return super().form_invalid(form)


class GenreDeleteView(DeleteView):
    template_name = 'forms/delete_genre_form.html'
    model = Genre
    success_url = reverse_lazy('genres')

    # def get(self, request, pk):
    #     if not Genre.objects.filter(id=pk).exists():
    #         return HttpResponse('Object does not exists.')
    #     return super().get(request)


class GreetingView(View):
    greeting = "Good morning"

    def get(self, request):
        return HttpResponse(self.greeting)


class MovieDetailView(DetailView):
    template_name = "movie_detailed_view.html"
    model = Movie
