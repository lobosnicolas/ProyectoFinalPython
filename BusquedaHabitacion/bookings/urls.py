from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def mi_vista(HttpResponsee):
    return HttpResponse("<h1>hola<h1>")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("bookings/", mi_vista)
]
