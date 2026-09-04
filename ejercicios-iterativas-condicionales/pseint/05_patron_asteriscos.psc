// Ejercicio Basico 5: Impresion de patrones simples
// Imprime N lineas: la linea i contiene i asteriscos.

Algoritmo PatronAsteriscos
	Definir n, i, j Como Entero
	Definir linea Como Caracter

	Repetir
		Escribir "Ingrese la cantidad de lineas (N): "
		Leer n
		Si n <= 0 Entonces
			Escribir "El numero debe ser mayor que cero. Intente de nuevo."
		FinSi
	Hasta Que n > 0

	Para i <- 1 Hasta n Con Paso 1 Hacer
		linea <- ""
		Para j <- 1 Hasta i Con Paso 1 Hacer
			linea <- Concatenar(linea, "*")
		FinPara
		Escribir linea
	FinPara
FinAlgoritmo
