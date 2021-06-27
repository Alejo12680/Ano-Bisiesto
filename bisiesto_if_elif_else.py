'''
Escenario
Como seguramente sabrás, debido a algunas razones astronómicas, el año pueden ser bisiesto o común . Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.

Desde la introducción del calendario gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

Si el número del año no es divisible entre cuatro, es un año común.
De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
De lo contrario, si el número del año no es divisible entre 400, es un año común.
De lo contrario, es un año bisiesto.
Observa el código en el editor: solo lee un número de año y debe completarse con las instrucciones que implementan la prueba que acabamos de describir.

El código debe mostrar uno de los dos mensajes posibles, que son Año bisiesto o Año común, según el valor ingresado.

Sería bueno verificar si el año ingresado cae en la era gregoriana y emitir una advertencia de lo contrario: No dentro del período del calendario gregoriano. Consejo: utiliza los operadores != y %.
'''

ano = int(input("Introduzca un año:"))

if ano<1582:
	print("No entra en el período del calendario gregoriano")

elif ano % 4!=0:
	print("Año normal")
elif ano % 4==0 and ano % 100!=0:
	print("Año bisiesto")
elif ano % 4==0 and ano % 100==0 and ano % 400!=0:
	print("Año normal")
elif ano % 4==0 and ano % 100==0 and ano % 400==0:
	print("Año bisiesto")


#Combinaciones Anidadas (Version de codigo nuevo un poco mas lento con el "NOT")

ano = int(input("Introduzca un año:"))

if not ano % 4:
	if not ano % 100:
		if not ano % 400:
			print("Es Bisiesto")
		else:
			print("No es Bisiesto")
	else:
		print("Es Bisiesto")
else:
	print("No se Bisiesto")

'''
Mejora del codigo del año bisiesto con una sola condición

En lenguaje natural podemos decir que un año es bisiesto si «es múltiplo de 4 y además no es múltiplo de 100 o lo es de 400. Siendo un poco más formales, pero solo un poco, y siendo A la condición de ser múltiplo de 4, B la condición de ser múltiplo de 100 y C la condición de ser múltiplo de 400 podemos decir que un año es bisiesto si se cumple que A y (no B o C).
'''

ano = int(input("Introduzca un año:"))

if ano % 4==0 and (ano % 100 !=0 or ano % 400==0):
	print("Es Año Bisiesto")

else:
	print("No es Año Bisiesto")

'''
Mejorando el código y creando una función:
a primera mejora consiste en eliminar las comparaciones == y !=. Pero, ¿podemos hacer esto? Pues claro. Python considera que cualquier número diferente de 0 es True y que el 0 es False. Así, de esta manera, y teniendo en cuenta que el operador % nos devuelve un número que se puede considerar un valor booleano, podemos hacer las siguientes sustituciones:

año % 4 == 0 por not año % 4.
año % 100 != 0 por año % 100.
año % 400 == 0 por not año % 400.
Esta mejora podemos aplicarla en cualquiera de las versiones que te he presentado aquí. Aplicada a la última versión la condición completa nos quedaría de la siguiente manera: not año % 4 and (año % 100 or not año % 400).

La segunda mejora consiste en usar el operador condicional ternario de Python que nos permitirá escribir la condición y el resultado en una sola línea.
'''
ano = int(input("Introduzca un año:"))

print("Es Bisiesto" if not ano % 4 and (ano % 100 or not ano % 400) else "No Bisiesto")

# Solo nos queda ya ubicar ese código dentro de una función que reciba el año como parámetro

def bisisesto(ano):
	return not ano % 4 and (ano % 100 or not ano % 400)

#Esto nos servira para hacer un recorrido con un FOR y ver los años bisiestos entre una fecha y otra fecha

def bisisesto(ano):
	return not ano % 4 and (ano % 100 or not ano % 400)

for ano in range(1800, 2021):
	if bisisesto(ano):# la funsion 
		print(ano, end=" ")

'''
Comprobar año bisiesto con el módulo calendar de Python:
Python ya incorpora una función que lo hace por nosotros.

Dentro del módulo calendar, que está destinado a realizar operaciones con fechas, existe una función llamada isleap, entre otras muchas, que hace exactamente lo mismo que la función es_bisiesto que te acabo de proponer más arriba. Para utilizarla basta con importar la función y utilizarla como queramos. Te lo muestro con el ejemplo anterior:
'''

from calendar import isleap #llamado al modulo 

for ano in range(1800,2021):
	if isleap(ano): # la funsión de python
		print(ano, end=" ")