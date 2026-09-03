# Pseudocódigo — Gustos Musicales

Descripción en pseudocódigo (español, estilo estructurado) de la lógica del sitio
implementado en `index.html`, `css/style.css` y `js/script.js`.

---

## 1. Estructuras de datos

```
ESTRUCTURA Genero
    id          : texto        // "rock", "pop", ...
    icono       : texto        // emoji representativo
    nombre      : texto
    descripcion : texto
    artistas    : lista de texto
FIN ESTRUCTURA

ESTRUCTURA Opcion
    texto    : texto
    puntajes : mapa <idGenero -> entero>   // cuánto suma esta opción a cada género
FIN ESTRUCTURA

ESTRUCTURA Pregunta
    enunciado : texto
    opciones  : lista de Opcion
FIN ESTRUCTURA

CONSTANTE GENEROS   : lista de Genero    // 8 géneros: rock, pop, reggaetón, jazz,
                                         // electrónica, hip-hop, clásica, salsa
CONSTANTE PREGUNTAS : lista de Pregunta  // 5 preguntas del test
```

---

## 2. Programa principal

```
INICIO Programa
    // El script se ejecuta cuando el navegador termina de leer el HTML
    RenderizarGeneros()
    ConstruirFiltrosYSelector()
    RenderizarArtistas("todos")
    IniciarTest()
    RegistrarEventosFormulario()
    RegistrarEventosMenuMovil()
    EscribirAnioEnPie()
FIN Programa
```

---

## 3. Catálogo de géneros

```
PROCEDIMIENTO RenderizarGeneros()
    contenedor <- BuscarElemento("genreGrid")
    PARA CADA g EN GENEROS HACER
        tarjeta <- CrearElemento("div", clase: "genre-card")
        tarjeta.contenido <- icono + nombre + descripción de g
        AgregarHijo(contenedor, tarjeta)
    FIN PARA
FIN PROCEDIMIENTO
```

---

## 4. Artistas: filtros y listado

```
PROCEDIMIENTO ConstruirFiltrosYSelector()
    filtros  <- BuscarElemento("artistFilters")
    selector <- BuscarElemento("favGenre")     // <select> del formulario

    // Botón inicial "Todos", marcado como activo
    AgregarHijo(filtros, BotonFiltro(texto: "Todos", genero: "todos", activo: VERDADERO))

    PARA CADA g EN GENEROS HACER
        AgregarHijo(filtros,  BotonFiltro(texto: g.icono + g.nombre, genero: g.id))
        AgregarHijo(selector, Opcion(valor: g.id, texto: g.nombre))
    FIN PARA

    // Delegación de eventos: un solo escucha para todos los botones
    AL HACER CLIC EN filtros CON evento e HACER
        boton <- AncestroMasCercano(e.objetivo, ".filter-btn")
        SI boton ES NULO ENTONCES SALIR
        PARA CADA b EN BotonesDe(filtros) HACER QuitarClase(b, "active") FIN PARA
        AgregarClase(boton, "active")
        RenderizarArtistas(boton.genero)
    FIN AL
FIN PROCEDIMIENTO


PROCEDIMIENTO RenderizarArtistas(idGenero)
    grid <- BuscarElemento("artistGrid")
    Vaciar(grid)

    SI idGenero = "todos" ENTONCES
        seleccion <- GENEROS
    SINO
        seleccion <- FiltrarGeneros(GENEROS, POR id = idGenero)
    FIN SI

    PARA CADA g EN seleccion HACER
        PARA CADA artista EN g.artistas HACER
            tarjeta <- CrearElemento("div", clase: "artist-card")
            tarjeta.contenido <- g.icono + artista + g.nombre
            AgregarHijo(grid, tarjeta)
        FIN PARA
    FIN PARA
FIN PROCEDIMIENTO
```

---

## 5. Test de gusto musical

Estado global del test:

```
VARIABLE preguntaActual : entero
VARIABLE puntajes       : mapa <idGenero -> entero>
```

### 5.1 Inicio / reinicio

```
PROCEDIMIENTO IniciarTest()
    preguntaActual <- 0
    puntajes       <- mapa vacío
    Ocultar(bloqueResultado)
    Mostrar(bloquePregunta)
    RenderizarPregunta()
FIN PROCEDIMIENTO
```

### 5.2 Mostrar una pregunta

```
PROCEDIMIENTO RenderizarPregunta()
    p <- PREGUNTAS[preguntaActual]

    // Barra de progreso: 0 % en la primera pregunta, 80 % en la quinta
    barraProgreso.ancho <- (preguntaActual / Longitud(PREGUNTAS)) * 100 %

    bloquePregunta.contenido <- p.enunciado
    PARA CADA (opcion, i) EN p.opciones HACER
        AgregarHijo(bloquePregunta, Boton(texto: opcion.texto, indice: i))
    FIN PARA

    PARA CADA boton EN OpcionesDe(bloquePregunta) HACER
        AL HACER CLIC HACER ResponderOpcion(p, boton.indice) FIN AL
    FIN PARA
FIN PROCEDIMIENTO
```

### 5.3 Registrar respuesta y avanzar

```
PROCEDIMIENTO ResponderOpcion(pregunta, indice)
    opcion <- pregunta.opciones[indice]

    // Acumular los puntos que la opción aporta a cada género
    PARA CADA (idGenero, valor) EN opcion.puntajes HACER
        puntajes[idGenero] <- ValorOCero(puntajes[idGenero]) + valor
    FIN PARA

    preguntaActual <- preguntaActual + 1

    SI preguntaActual < Longitud(PREGUNTAS) ENTONCES
        RenderizarPregunta()
    SINO
        MostrarResultado()
    FIN SI
FIN PROCEDIMIENTO
```

### 5.4 Calcular y mostrar el resultado

```
PROCEDIMIENTO MostrarResultado()
    barraProgreso.ancho <- 100 %
    Ocultar(bloquePregunta)
    Mostrar(bloqueResultado)

    // Búsqueda del máximo: gana el género con más puntos acumulados.
    // En caso de empate se conserva el primero encontrado.
    ganador <- PrimeraClave(puntajes)
    PARA CADA (id, valor) EN puntajes HACER
        SI valor > puntajes[ganador] ENTONCES
            ganador <- id
        FIN SI
    FIN PARA

    genero <- BuscarGeneroPorId(ganador)
    SI genero ES NULO ENTONCES genero <- GENEROS[0] FIN SI   // respaldo

    textoResultado      <- genero.icono + " " + genero.nombre
    descripcionResultado <- genero.descripcion
FIN PROCEDIMIENTO


AL HACER CLIC EN botonReintentar HACER
    IniciarTest()
FIN AL
```

---

## 6. Formulario de contacto

```
PROCEDIMIENTO RegistrarEventosFormulario()
    AL ENVIAR formularioContacto CON evento e HACER
        e.PrevenirEnvioPorDefecto()          // no recarga la página
        Mostrar(mensajeConfirmacion)         // "¡Gracias por compartir...!"
        LimpiarCampos(formularioContacto)
        ESPERAR 4 segundos LUEGO Ocultar(mensajeConfirmacion)
    FIN AL
FIN PROCEDIMIENTO
```

> Nota: la validación de nombre y correo la hace el navegador mediante los
> atributos `required` y `type="email"` del HTML. No hay envío a un servidor.

---

## 7. Menú móvil y pie de página

```
PROCEDIMIENTO RegistrarEventosMenuMovil()
    AL HACER CLIC EN botonMenu HACER
        AlternarClase(listaEnlaces, "open")   // abre o cierra el menú
    FIN AL

    PARA CADA enlace EN EnlacesDe(listaEnlaces) HACER
        AL HACER CLIC HACER QuitarClase(listaEnlaces, "open") FIN AL
    FIN PARA
FIN PROCEDIMIENTO


PROCEDIMIENTO EscribirAnioEnPie()
    elementoAnio.texto <- AnioActual()
FIN PROCEDIMIENTO
```

---

## 8. Flujo del usuario (resumen)

```
Usuario entra al sitio
   -> ve el hero y navega por el menú
   -> explora la sección "Géneros" (8 tarjetas)
   -> hace el test:
        repetir 5 veces: leer pregunta, elegir una opción, sumar puntos
        al terminar: mostrar el género con mayor puntaje
        opcional: reiniciar el test
   -> filtra artistas por género (o "Todos")
   -> envía el formulario y recibe una confirmación en pantalla
```
