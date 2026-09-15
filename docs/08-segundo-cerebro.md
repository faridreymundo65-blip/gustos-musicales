# 8. Segundo cerebro: tu conocimiento, conectado

Una base de conocimiento personal donde vive lo que aprendes, lo que decides y lo
que sabes de cada cliente. En `segundo-cerebro/`, listo para abrir con Obsidian.

## Por qué en archivos Markdown

Son archivos de texto plano. Los lee Obsidian, los lee tu editor, los lee Claude
Code y los seguirás pudiendo leer dentro de diez años. Sin formato propietario y
sin depender de que una empresa siga existiendo.

Que Claude Code pueda leerlos y escribirlos es la parte que convierte un archivo
de notas en un sistema: el mismo agente que trabaja en tu código consulta lo que
decidiste hace tres meses.

## El método PARA

```
00-Inbox/       Todo lo que entra. Sin pensar, sin clasificar.
10-Proyectos/   Objetivo concreto + fecha de fin
20-Areas/       Responsabilidades continuas (clientes, finanzas, salud)
30-Recursos/    Material de consulta
40-Archivo/     Terminado o ya irrelevante
90-Plantillas/  Plantillas de notas
```

La pregunta que distingue proyecto de área: **¿esto se puede terminar?** Una web
para un cliente se termina (proyecto). "Clientes" no se termina nunca (área).

## Las dos reglas que sostienen el sistema

### 1. Capturar sin fricción
Toda idea va a `00-Inbox/`. No te pares a decidir dónde ponerla: esa duda de tres
segundos es exactamente lo que hace que dejes de capturar. Ya se ordenará.

### 2. Enlazar siempre
Una nota sin enlaces es una nota perdida. El valor no está en las notas, está en
las conexiones: `[[nombre-de-la-nota]]`.

Por eso existe `MOC-Inicio.md` (mapa de contenido): el punto desde el que se
llega a todo lo demás.

## Cómo se usa desde Claude Code

```
/capturar-nota
```
Elige la carpeta correcta, aplica la plantilla, rellena el frontmatter, busca si
ya existe una nota del mismo tema y la enlaza.

Y para el mantenimiento semanal, el subagente:

> "Lanza organizador-notas para procesar el inbox"

Vacía `00-Inbox/`, detecta duplicados, enlaza huérfanas y te dice qué necesita tu
decisión. Nunca borra nada por su cuenta.

## La revisión semanal (10 minutos)

1. Vaciar `00-Inbox/`.
2. Actualizar el estado de cada proyecto activo.
3. Archivar lo terminado.
4. Enlazar las notas sueltas.

Diez minutos a la semana. Sin esto, en dos meses tienes un cajón desastre en vez
de un segundo cerebro — y un cajón desastre no lo consulta nadie, ni tú ni la IA.

## Qué anotar (y qué no)

**Sí**: decisiones y por qué las tomaste, aprendizajes con su contexto, datos de
clientes, plantillas que te funcionaron, errores y cómo los resolviste.

**No**: cosas que puedes buscar en Google en diez segundos, copias enteras de
artículos, tareas sueltas (para eso hay listas de tareas, no notas).

El filtro: **¿mi yo de dentro de seis meses agradecerá esto?**
