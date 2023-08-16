# Tercera-pre-entregaConaLipianArlette
Desarrollar una WEB Django con patrón MVT subida a Github.



Nombre: Arlette Cona Lipian


Preentrega: 3


Fecha entrega:17-08-2023



Proyecto:este proyecto consiste en un registro web, con el objetivo de almacenar datos relacionados al
mundo del cine. Para esta instancia se consideró en el modelo tener un repo de películas, directores y
productoras.
Inicialmente se pensó como un blog de cine, que con el tiempo espero ir mejorando y trabajando.



Modelos:
1.pelicula
	Atributos
	 nombre: charfield
	 fecha_estreno: datefield
	 productora: charfield
	 genero: charfield

2.director
	Atributos
	 nombre:charfield
	 nacionalidad:charfield

3.productoras
	Atributos
	 nombre:charfield
	 pais: charfield




Funcionalidades:


la herencia HTML viene desde base.html 
about es el home.html
/pelicula/         muestra todos los datos que hay en el modelo pelicula
/director/	   muestra todos los datos que hay en el modelo director
/productoras/	   muestra todos los datos que hay en el modelo productoras
/buscar/    	   hay un botón buscar que muestra un patron buscado en el modelo de peliculas

se crea formularios para insertar datos a todas las clases en models.py
/peliculaForm2/    permite agregar una pelicula nueva al motor de base de datos
/directorForm2/	   permite agregar un director nuevo al motor de base de datos
/productoraForm2/  permite agrear una nueva productora al motor de base de datos





