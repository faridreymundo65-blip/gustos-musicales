// Ejercicio Intermedio 5: Juego de adivinanza con pistas
// El usuario intenta adivinar un numero secreto entre 1 y 100.

Algoritmo JuegoAdivinanza
	Definir secreto, intento, intentos Como Entero
	Definir acerto Como Logico

	secreto <- Aleatorio(1, 100)
	intentos <- 0
	acerto <- Falso

	Escribir "Adivine el numero secreto entre 1 y 100."

	Mientras acerto = Falso Hacer
		Escribir "Su intento: "
		Leer intento

		Si intento < 1 O intento > 100 Entonces
			Escribir "El numero debe estar entre 1 y 100."
		SiNo
			intentos <- intentos + 1

			Si intento = secreto Entonces
				acerto <- Verdadero
			SiNo
				Si intento < secreto Entonces
					Escribir "El numero buscado es MAYOR que ", intento
				SiNo
					Escribir "El numero buscado es MENOR que ", intento
				FinSi
			FinSi
		FinSi
	FinMientras

	Escribir "Correcto! El numero era ", secreto
	Escribir "Lo lograste en ", intentos, " intento(s)."
FinAlgoritmo
