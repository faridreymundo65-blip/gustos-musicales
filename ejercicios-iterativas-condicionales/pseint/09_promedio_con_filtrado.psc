// Ejercicio Intermedio 4: Calculadora de promedio con filtrado
// Lee calificaciones hasta ingresar un numero negativo.
// Ignora en la suma y el conteo las notas menores a 5 (reprobatorias).

Algoritmo PromedioConFiltrado
	Definir nota, suma, promedio Como Real
	Definir contadas, ignoradas Como Entero

	suma <- 0
	contadas <- 0
	ignoradas <- 0

	Escribir "Ingrese las calificaciones. Un numero negativo finaliza el ingreso."

	Escribir "Calificacion: "
	Leer nota

	Mientras nota >= 0 Hacer
		Si nota >= 5 Entonces
			suma <- suma + nota
			contadas <- contadas + 1
		SiNo
			ignoradas <- ignoradas + 1
			Escribir "  (Nota reprobatoria: no se toma en cuenta)"
		FinSi

		Escribir "Calificacion: "
		Leer nota
	FinMientras

	Escribir "--- Resultados ---"
	Escribir "Notas consideradas: ", contadas
	Escribir "Notas ignoradas:    ", ignoradas

	Si contadas > 0 Entonces
		promedio <- suma / contadas
		Escribir "Promedio (solo notas >= 5): ", promedio
	SiNo
		Escribir "No se ingresaron notas aprobatorias, no hay promedio."
	FinSi
FinAlgoritmo
