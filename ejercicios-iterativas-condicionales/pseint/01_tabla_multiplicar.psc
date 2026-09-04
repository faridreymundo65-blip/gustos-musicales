// Ejercicio Basico 1: Tabla de multiplicar
// Solicita un numero entero y muestra su tabla de multiplicar del 1 al 10.

Algoritmo TablaDeMultiplicar
	Definir numero, i, resultado Como Entero

	Escribir "Ingrese un numero entero: "
	Leer numero

	Escribir "Tabla de multiplicar del ", numero, ":"

	Para i <- 1 Hasta 10 Con Paso 1 Hacer
		resultado <- numero * i
		Escribir numero, " x ", i, " = ", resultado
	FinPara
FinAlgoritmo
