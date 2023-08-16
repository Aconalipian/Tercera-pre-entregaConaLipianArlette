
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    #cuando no venga nada en la ruta, redirige todo a app
    path('', include('app.urls')),
]
