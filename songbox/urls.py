"""
URL configuration for songbox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("api/v1/movies",views.MovieViewSetView,basename="movies")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("helloworld/",views.HelloWorldView.as_view()),
    path("morning/",views.MorningView.as_view()),
    path("addition/",views.AdditionView.as_view()),
    path("bmi/",views.BmiView.as_view()),
    path("calories/",views.CalorieView.as_view()),
    path("api/albums/",views.AlbumListView.as_view()),
    path("api/movies/",views.MovieListCreateView.as_view()),
    path("api/movies/<int:pk>/",views.MovieRetriveUpdateDestroyView.as_view()),
    # path("api/genres/",views.GenreListView.as_view()),



]+router.urls
