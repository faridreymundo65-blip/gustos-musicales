// Ejercicio Basico 3: Contador regresivo
// Imprime una cuenta regresiva desde el numero ingresado hasta 0.

Algoritmo ContadorRegresivo
	Definir n, i Como Entero

	Repetir
		Escribir "Ingrese un numero entero positivo: "
		Leer n
		Si n <= 0 Entonces
			Escribir "El numero debe ser mayor que cero. Intente de nuevo."
		FinSi
	Hasta Que n > 0

	Escribir "Cuenta regresiva:"
	Para i <- n Hasta 0 Con Paso -1 Hacer
		Escribir i
	FinPara

	Escribir "Despegue!"
FinAlgoritmo
