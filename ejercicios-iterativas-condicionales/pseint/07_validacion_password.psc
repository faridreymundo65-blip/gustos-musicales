// Ejercicio Intermedio 2: Validacion de contrasena con intentos limitados
// Permite un maximo de 3 intentos para ingresar la contrasena correcta.

Algoritmo ValidacionPassword
	Definir claveCorrecta, intento Como Caracter
	Definir intentos, maxIntentos Como Entero
	Definir acceso Como Logico

	claveCorrecta <- "python2024"
	maxIntentos <- 3
	intentos <- 0
	acceso <- Falso

	Mientras intentos < maxIntentos Y acceso = Falso Hacer
		Escribir "Ingrese la contrasena: "
		Leer intento
		intentos <- intentos + 1

		Si intento = claveCorrecta Entonces
			acceso <- Verdadero
		SiNo
			Si intentos < maxIntentos Entonces
				Escribir "Contrasena incorrecta. Le quedan ", maxIntentos - intentos, " intento(s)."
			FinSi
		FinSi
	FinMientras

	Si acceso = Verdadero Entonces
		Escribir "Acceso concedido. Bienvenido!"
	SiNo
		Escribir "Acceso bloqueado: se agotaron los ", maxIntentos, " intentos."
	FinSi
FinAlgoritmo
