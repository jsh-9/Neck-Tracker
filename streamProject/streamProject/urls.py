from django.contrib import admin
from django.urls import path
from django.urls import include  # new
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('streamApp.urls'))  # new
]