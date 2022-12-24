Hola:
Os dejo en este repo mis soluciones de los ejerciocios de SD sobre map-reduce. Algunos detalles a considerar:
+ Ojo a utilizar el python correcto. En la línea de la almohadilla del principio de los .py, debéis poner
los path correspondientes a vuestro intérprete. Si tenéis un Ubuntu, se parecerán al mío y os valdrá con lo que pone
en los fricheros tal como están, pero no dejéis de comprobarlo.
+ Ojo porque si os planteáis ejecutar esto en el cluster de Horton local que tenemos, eso no va a valer. De hecho, lo
que hay instalado por defecto es python2, así que, además de modificar adecuadamente la línea de la almohadilla, deberéis
quitar todos los paréntesis de los "print" que haya en el código. Así son las cosas. En Python2, el print iba sin
paréntesis.
+ He dejado en cada folder algunos ficheros que pueden servir para probar así como unos ficheros de prueba que hacen
el trabajo completo y lo dejan en un fichero de resultado. Podéis borrarlo y ejecutar los "prueba.sh". Veréis que lo
vuelve a crear.
+ En el ejercicio de "books", he tenido que usar unas opciones un poco raras del sort. Si no, no me lo ordenaba bien.
¡Y la ordenación es crítica!
+ En el de matrices, que es, sin duda, el más tricky, he dejado algunos prints que pdéis descomentar, si queréis
ir viendo lo que hace en cada paso. Recordad eliminar los paréntesis si os vais a Horton.
+ Otra cosa tricky de ese ejercicio es que la entrada no es completa (el matrix.json está incompleto), pero aún así el
reducer puede funcionar. He visto que las matrices tienen 5 columnas (a) y 5 filas (b), así que he fijado el valor
a huevo en el código. Esto es una chapuza, y como mínimo tendría que pasarlo como parámetro al main para que el código 
sirviera de forma general para cualquier matriz, pero bueno...

¡Ánimo! Espero que os sirva de ayuda