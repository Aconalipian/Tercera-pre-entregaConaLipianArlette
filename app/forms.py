from django import forms

class f_peliculaForm(forms.Form):
    nombre=forms.CharField(max_length=50, required=True)
    fecha_estreno=forms.DateField(required=True)
    productora=forms.CharField(max_length=50,required=True)
    genero=forms.CharField(max_length=50, required=True)


class f_directorForm(forms.Form):
    nombre=forms.CharField(max_length=50, required=True)
    nacionalidad=forms.CharField(max_length=50, required=True)



class f_productorasForm(forms.Form):
    nombre=forms.CharField(max_length=50, required=True)
    pais=forms.CharField(max_length=50, required=True)