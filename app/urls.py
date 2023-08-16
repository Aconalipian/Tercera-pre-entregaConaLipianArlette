from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
   path('', Home, name="home" ),
   path('pelicula/', Pelicula, name="pelicula" ),
   path('director/', Director, name="director" ),
   path('productoras/', Productoras, name="productoras" ),
   path('buscar/', buscarForm, name="buscar" ),

   #formularios para guardar datos en el motor
   path('peliculaForm/', peliculaForm, name="pelicula_form" ),
   path('directorForm/', directorForm, name="director_Form" ),
   path('productoraForm/', productoraForm, name="productora_Form" ),

   path('peliculaForm2/', peliculaForm2, name="pelicula_Form2" ),
   path('directorForm2/', directorForm2, name="director_Form2" ),
   path('productoraForm2/', productoraForm2, name="productora_Form2" ),

   #formularios de búsqueda
   path('buscar/', buscarForm, name="buscar_Form" ),
   path('buscar2/', buscar2, name="buscar2" ),



   
]
