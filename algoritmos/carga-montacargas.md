# Algoritmo: Carga de Montacargas

Control de carga de un montacargas con capacidad máxima de 1000 kg.

## Versión original

```
Algoritmo CargaMontacargas

    CAPACIDAD_MAX <- 1000
    total_peso <- 0
    cajas_aceptadas <- 0
    continuar <- Verdadero

    Mientras continuar Hacer
        Escribir "Ingrese peso de la caja (kg):"
        Leer peso

        Si total_peso + peso <= CAPACIDAD_MAX Entonces
            total_peso <- total_peso + peso
            cajas_aceptadas <- cajas_aceptadas + 1
            Escribir "Caja aceptada."
        Sino
            Escribir "¡ALERTA! Excede capacidad. Caja rechazada."
            continuar <- Falso
        FinSi
    FinMientras

    Escribir "Carga total:", total_peso, "kg en", cajas_aceptadas, "cajas."

FinAlgoritmo
```

### Prueba de escritorio (pesos: 300, 400, 200, 500)

| Caja | peso | total_peso + peso | ¿<= 1000? | total_peso | cajas_aceptadas | continuar |
|------|------|-------------------|-----------|------------|-----------------|-----------|
| 1    | 300  | 300               | Sí        | 300        | 1               | Verdadero |
| 2    | 400  | 700               | Sí        | 700        | 2               | Verdadero |
| 3    | 200  | 900               | Sí        | 900        | 3               | Verdadero |
| 4    | 500  | 1400              | No        | 900        | 3               | Falso     |

Salida: `Carga total: 900 kg en 3 cajas.`

### Observaciones

1. **La única salida del bucle es un rechazo.** Si el operario terminó de cargar,
   no tiene forma de cerrar el proceso: debe ingresar una caja que no quepa.
2. **Un rechazo cancela toda la carga.** Si quedan 100 kg libres y llega una caja
   de 300 kg, se cierra el proceso aunque después viniera una de 50 kg que sí cabía.
3. **No valida el peso leído.** Un peso de 0 o negativo se acepta; un negativo
   incluso reduce el total acumulado.
4. **No informa la capacidad disponible**, que es el dato que el operario necesita
   para decidir la siguiente caja.

## Versión corregida

```
Algoritmo CargaMontacargas

    CAPACIDAD_MAX <- 1000
    total_peso      <- 0
    cajas_aceptadas <- 0
    cajas_rechazadas <- 0
    continuar <- Verdadero

    Escribir "=== Control de carga (capacidad:", CAPACIDAD_MAX, "kg) ==="

    Mientras continuar Hacer

        disponible <- CAPACIDAD_MAX - total_peso
        Escribir "Capacidad disponible:", disponible, "kg"

        // --- Lectura con validación ---
        Repetir
            Escribir "Ingrese peso de la caja en kg (0 para terminar):"
            Leer peso
            Si peso < 0 Entonces
                Escribir "Peso inválido: debe ser un número positivo."
            FinSi
        Hasta Que peso >= 0

        Si peso = 0 Entonces
            // El operario decide cerrar la carga
            continuar <- Falso
        Sino
            Si total_peso + peso <= CAPACIDAD_MAX Entonces
                total_peso      <- total_peso + peso
                cajas_aceptadas <- cajas_aceptadas + 1
                Escribir "Caja aceptada. Total:", total_peso, "kg"

                Si total_peso = CAPACIDAD_MAX Entonces
                    Escribir "Capacidad máxima alcanzada. Se cierra la carga."
                    continuar <- Falso
                FinSi
            Sino
                cajas_rechazadas <- cajas_rechazadas + 1
                Escribir "¡ALERTA! Excede capacidad por",
                         (total_peso + peso) - CAPACIDAD_MAX, "kg. Caja rechazada."
                Escribir "Puede intentar con una caja de hasta", disponible, "kg."
                // No se corta el proceso: quizá la siguiente caja sí quepa
            FinSi
        FinSi

    FinMientras

    Escribir "--- Resumen de la carga ---"
    Escribir "Carga total:", total_peso, "kg en", cajas_aceptadas, "cajas."
    Escribir "Cajas rechazadas:", cajas_rechazadas
    Escribir "Capacidad sin usar:", CAPACIDAD_MAX - total_peso, "kg"

FinAlgoritmo
```

### Cambios respecto al original

| Problema | Solución |
|----------|----------|
| No había forma de terminar sin fallar | El peso `0` funciona como centinela de salida |
| Un rechazo cancelaba todo | El rechazo solo descarta esa caja; el bucle continúa |
| Pesos negativos aceptados | Bucle `Repetir ... Hasta Que` que valida antes de procesar |
| Sin información al operario | Muestra capacidad disponible y cuántos kg se excedió |
| Resumen incompleto | Agrega cajas rechazadas y capacidad sin usar |

### Prueba de escritorio de la versión corregida (300, 400, 500, 200, 0)

| peso | disponible | Resultado | total_peso | aceptadas | rechazadas |
|------|-----------|-----------|------------|-----------|------------|
| 300  | 1000      | Aceptada  | 300        | 1         | 0          |
| 400  | 700       | Aceptada  | 700        | 2         | 0          |
| 500  | 300       | Rechazada (excede por 200) | 700 | 2 | 1     |
| 200  | 300       | Aceptada  | 900        | 3         | 1          |
| 0    | 100       | Fin       | 900        | 3         | 1          |

Salida final: carga de 900 kg en 3 cajas, 1 caja rechazada, 100 kg sin usar.

La diferencia clave: la caja de 200 kg que el algoritmo original habría perdido
al cortar el proceso, aquí sí se carga.
