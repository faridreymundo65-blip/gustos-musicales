// Ejercicio Basico 2: Suma de los primeros N numeros
// Pide un entero positivo N y calcula la suma de 1 hasta N.

Algoritmo SumaPrimerosN
	Definir n, i, suma Como Entero

	Repetir
		Escribir "Ingrese un numero entero positivo (N): "
		Leer n
		Si n <= 0 Entonces
			Escribir "El numero debe ser mayor que cero. Intente de nuevo."
		FinSi
	Hasta Que n > 0

	suma <- 0
	Para i <- 1 Hasta n Con Paso 1 Hacer
		suma <- suma + i
	FinPara

	Escribir "La suma de los numeros del 1 al ", n, " es: ", suma
FinAlgoritmo
