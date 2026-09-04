// Ejercicio Intermedio 1: Clasificador de numeros pares e impares
// Cuenta cuantos numeros son pares, impares y cuantos son cero.

Algoritmo ClasificadorParesImpares
	Definir cantidad, i, numero Como Entero
	Definir pares, impares, ceros Como Entero

	Repetir
		Escribir "Cuantos numeros desea ingresar? "
		Leer cantidad
		Si cantidad <= 0 Entonces
			Escribir "Debe ingresar al menos un numero."
		FinSi
	Hasta Que cantidad > 0

	pares <- 0
	impares <- 0
	ceros <- 0

	Para i <- 1 Hasta cantidad Con Paso 1 Hacer
		Escribir "Numero ", i, ": "
		Leer numero

		Si numero = 0 Entonces
			ceros <- ceros + 1
		SiNo
			Si numero MOD 2 = 0 Entonces
				pares <- pares + 1
			SiNo
				impares <- impares + 1
			FinSi
		FinSi
	FinPara

	Escribir "--- Resumen ---"
	Escribir "Pares:   ", pares
	Escribir "Impares: ", impares
	Escribir "Ceros:   ", ceros
FinAlgoritmo
