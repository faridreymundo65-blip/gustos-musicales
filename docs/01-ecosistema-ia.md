# 1. El ecosistema de IA: qué herramienta para qué

El error más caro es usar la herramienta equivocada: pedirle a un chat que
gestione archivos, o abrir un entorno de desarrollo para redactar un correo.

## El mapa

| Herramienta | Para qué sirve | Cuándo NO usarla |
|---|---|---|
| **Claude (chat)** | Pensar, redactar, decidir, analizar un texto | Cuando el resultado debe quedar en archivos |
| **Claude Code** | Trabajar sobre archivos y carpetas reales, ejecutar comandos, automatizar | Para una pregunta suelta |
| **Cowork** | Colaborar sobre un espacio de trabajo compartido | Trabajo individual en tu máquina |
| **Claude Design** | Maquetas visuales que luego retocas a mano | Cuando ya sabes el HTML que quieres |
| **Artifacts** | Una página o app que compartes por enlace | Un archivo que vive en tu repo |

## La diferencia que importa

Un chat **te devuelve texto**. Claude Code **cambia el estado de tu disco**:
crea archivos, edita, ejecuta comandos, hace commits. Por eso pide permisos, y
por eso puede trabajar mientras tú no estás.

Todo lo que ves en este repositorio —los dos sitios, las skills, los subagentes,
el vault— existe como archivos reales. Puedes abrirlos, versionarlos con git y
desplegarlos. Eso es lo que un chat no puede darte.

## Cómo encadenarlas en la práctica

1. **Chat**: decides el concepto y el público de una landing.
2. **Design**: generas una maqueta visual y la ajustas.
3. **Code**: la conviertes en HTML/CSS real dentro del repo, la revisas con el
   subagente `revisor-qa` y la publicas con la skill `publicar-web`.
4. **Code otra vez**: guardas lo aprendido en el segundo cerebro para el
   siguiente cliente.

El sistema completo no es una herramienta: es el encadenamiento. Cada pieza deja
un rastro que la siguiente aprovecha.

## Regla práctica

> ¿El resultado tiene que existir mañana, sin ti delante, en un archivo o una
> URL? → Claude Code.
> ¿Solo necesitas pensar mejor ahora mismo? → Chat.
