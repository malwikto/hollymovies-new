"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from accounts.models import Profile
from viewer.forms import MovieForm
from viewer.views import search, MoviesView, MovieCreateView, Hello, Contact, GenreCreateView, GreetingView, \
    MovieUpdateView, MovieDeleteView, MovieDetailView, GenreListView, GenreUpdateView, GenreDeleteView
from viewer.models import Genre, Movie
from viewer.admin import MovieAdmin, GenreAdmin

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Profile)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include('accounts.urls')),
    path("search/", search, name="search"),
    path("movies/new", MovieCreateView.as_view(success_url="/movies/"), name="create_movie"),
    path("movies/<int:pk>", MovieDetailView.as_view(), name="read_movie"),
    path("movies/<int:pk>/update", MovieUpdateView.as_view(), name="update_movie"),
    path("movies/<int:pk>/delete", MovieDeleteView.as_view(), name="delete_movie"),
    path("movies/", MoviesView.as_view(), name="movies"),
    path("genres/", GenreListView.as_view(), name="genres"),
    path("genres/<int:pk>/update", GenreUpdateView.as_view(), name="update_genre"),
    path("genres/<int:pk>/delete", GenreDeleteView.as_view(), name="delete_genre"),

    path("greeting/", GreetingView.as_view(greeting="Hello"), name="greeting"),
    path("new_genre/", GenreCreateView.as_view(success_url="/new_genre"), name="create_genre"),
    path("contact/", Contact.as_view(), name="contact"),
    path("", Hello.as_view(), name="hello"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
