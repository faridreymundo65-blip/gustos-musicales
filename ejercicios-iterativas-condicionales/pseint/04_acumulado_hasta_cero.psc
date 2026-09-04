// Ejercicio Basico 4: Acumulado hasta cero
// Suma numeros ingresados por el usuario hasta que se ingrese 0.

Algoritmo AcumuladoHastaCero
	Definir numero, total, cantidad Como Entero

	total <- 0
	cantidad <- 0

	Escribir "Ingrese numeros para sumar. Escriba 0 para terminar."

	Repetir
		Escribir "Numero: "
		Leer numero
		Si numero <> 0 Entonces
			total <- total + numero
			cantidad <- cantidad + 1
		FinSi
	Hasta Que numero = 0

	Escribir "Cantidad de numeros sumados: ", cantidad
	Escribir "Total acumulado: ", total
FinAlgoritmo
