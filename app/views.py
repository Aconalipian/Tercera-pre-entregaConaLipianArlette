from django.shortcuts import render
from django.http import HttpResponse

from .models import pelicula
from .models import director
from .models import productoras

from .models import *
from .forms import *




def Home(request):
    return render(request, "app/home.html")

def Pelicula(request):
    contexto = {'peliculas': pelicula.objects.all()}
    return render(request, "app/pelicula.html", contexto)

def Director(request):
    contexto = {'directores': director.objects.all()}
    return render(request, "app/director.html", contexto)


def Productoras(request):
    contexto = {'productora': productoras.objects.all()}
    return render(request, "app/productora.html", contexto)



#Acá se define cada formulario por modelo
def peliculaForm(request):
    if request.method == "POST":
        Peli = pelicula(nombre=request.POST['nombre'],
                            fecha_estreno=request.POST['fecha_estreno'],
                            productora=request.POST['productora'],
                            genero=request.POST['genero'])
        Peli.save()
        return HttpResponse("Se grabó exitosamente una nueva película!")
    return render(request,"app/peliculaForm.html")



def directorForm(request):
    if request.method == "POST":
        direc = director(nombre=request.POST['nombre'],
                        nacionalidad=request.POST['nacionalidad']
                            )
        direc.save()
        return HttpResponse("Se grabó exitosamente un nuevo director!")
    return render(request,"app/directorForm.html")



def productoraForm(request):
    if request.method == "POST":
        produc = productoras(nombre=request.POST['nombre'],
                        pais=request.POST['pais']
                            )
        produc.save()
        return HttpResponse("Se grabó exitosamente nueva productora!")
    return render(request,"app/productoraForm.html")


def peliculaForm2(request):
    if request.method == "POST":
        miForm= f_peliculaForm(request.POST)
        if miForm.is_valid():
            peli_nombre = miForm.cleaned_data.get('nombre')
            peli_fechaEstreno= miForm.cleaned_data.get('fecha_estreno')
            peli_productora= miForm.cleaned_data.get('productora')
            peli_genero=miForm.cleaned_data.get('genero')

            Peli = pelicula(nombre=peli_nombre,
                            fecha_estreno=peli_fechaEstreno,
                            productora=peli_productora,
                            genero=peli_genero)
            Peli.save()
            return render(request,"app/base.html")
    else:
        miForm=f_peliculaForm()

              
    return render(request,"app/peliculaForm2.html",{"form":miForm})




def directorForm2(request):
    if request.method == "POST":
        miForm= f_directorForm(request.POST)
        if miForm.is_valid():
            direc_nombre = miForm.cleaned_data.get('nombre')
            direc_nacionalidad=miForm.cleaned_data.get('nacionalidad')
            direc = director(nombre=request.POST['nombre'],
                        nacionalidad=request.POST['nacionalidad']
            )
            direc.save()
            return render(request,"app/base.html")
    else:
        miForm=f_directorForm()

            
    return render(request,"app/directorForm2.html",{"form":miForm})



def productoraForm2(request):
    if request.method == "POST":
        miForm= f_productorasForm(request.POST)
        if miForm.is_valid():
            produc_nombre = miForm.cleaned_data.get('nombre')
            produc_pais=miForm.cleaned_data.get('pais')

            produc = productoras(nombre=request.POST['nombre'],
                        pais=request.POST['pais']
                            )
            produc.save()
            return render(request,"app/base.html")
    else:
        miForm=f_directorForm()

    return render(request,"app/productoraForm2.html",{"form":miForm})



def buscarForm(request):
    return render(request, "app/buscar.html")




def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        peli = pelicula.objects.filter(nombre__icontains=patron)
        contexto= {"peliculas":peli, 'titulo': f"Películas encontradas con patrón: {patron}"}
        return render(request,"app/pelicula.html", contexto)
    return HttpResponse("No ha ingresado nada, favor escriba un valor a buscar")



