from django.contrib import admin
from django.urls import path
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blogpost.urls')),
]