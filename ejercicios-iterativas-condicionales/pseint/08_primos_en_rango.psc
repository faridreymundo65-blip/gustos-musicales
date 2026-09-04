// Ejercicio Intermedio 3: Numeros primos en un rango
// Recorre el rango [inicio, fin] e imprime unicamente los numeros primos.

Algoritmo PrimosEnRango
	Definir inicio, fin, numero, divisor, aux Como Entero
	Definir esPrimo Como Logico
	Definir encontrados Como Entero

	Escribir "Ingrese el inicio del rango: "
	Leer inicio
	Escribir "Ingrese el fin del rango: "
	Leer fin

	// Si el usuario invierte el rango, se intercambian los valores
	Si inicio > fin Entonces
		aux <- inicio
		inicio <- fin
		fin <- aux
	FinSi

	encontrados <- 0
	Escribir "Numeros primos entre ", inicio, " y ", fin, ":"

	Para numero <- inicio Hasta fin Con Paso 1 Hacer
		Si numero < 2 Entonces
			esPrimo <- Falso
		SiNo
			esPrimo <- Verdadero
			divisor <- 2
			Mientras divisor * divisor <= numero Y esPrimo = Verdadero Hacer
				Si numero MOD divisor = 0 Entonces
					esPrimo <- Falso
				FinSi
				divisor <- divisor + 1
			FinMientras
		FinSi

		Si esPrimo = Verdadero Entonces
			Escribir numero
			encontrados <- encontrados + 1
		FinSi
	FinPara

	Si encontrados = 0 Entonces
		Escribir "No se encontraron numeros primos en el rango."
	SiNo
		Escribir "Total de primos encontrados: ", encontrados
	FinSi
FinAlgoritmo
