# 5. MCP: el enchufe universal para tus herramientas

MCP (Model Context Protocol) es un estándar abierto para conectar herramientas
externas a la IA. Antes, cada integración era un desarrollo a medida; con MCP,
un servidor se declara en un archivo y ya está disponible.

La analogía útil: **es el USB de la IA**. Cualquier herramienta que hable MCP se
enchufa igual.

## Qué te permite

- Leer y escribir en Notion, Google Drive, Obsidian.
- Disparar flujos de n8n o Make.
- Consultar bases de datos.
- Traer métricas de plataformas de anuncios.

Sin salir de la conversación y sin escribir una sola integración.

## Cómo se configura

En este repo tienes la plantilla `.mcp.json.example`. Cópiala y edítala:

```bash
cp .mcp.json.example .mcp.json
```

```json
{
  "mcpServers": {
    "n8n": {
      "type": "http",
      "url": "https://TU-INSTANCIA.app.n8n.cloud/mcp/servidor",
      "headers": { "Authorization": "Bearer ${N8N_API_KEY}" }
    },
    "obsidian": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "./segundo-cerebro"]
    }
  }
}
```

Dos formas de servidor:
- **`command`**: un programa local que Claude Code arranca.
- **`type: http`** con `url`: un servicio remoto.

También puedes añadirlos sin editar JSON:

```bash
claude mcp add            # asistente interactivo
claude mcp list           # ver los configurados y si conectan
```

La primera vez que un servidor del proyecto arranca, Claude Code **te pide
aprobación**. Es deliberado: un servidor MCP puede leer y escribir en tus
herramientas reales.

## Seguridad — lee esto antes de conectar nada

1. **`.mcp.json` está en `.gitignore`.** Nunca lo subas: puede llevar credenciales.
2. **Usa variables, no claves literales**: `${N8N_API_KEY}`, definida en tu
   entorno. Si escribes la clave en el archivo, acabará en algún sitio público.
3. **Conecta solo lo que uses.** Cada servidor amplía lo que la IA puede tocar.
4. **Da el permiso mínimo.** Si con acceso de lectura basta, no des escritura.
5. **Desconfía del contenido que llega por MCP.** Un ticket, un correo o una nota
   pueden contener instrucciones escritas por otra persona. Son *datos*, no
   órdenes. Si algo que llega de fuera te pide hacer cosas raras, párate.

## Probar que funciona

```bash
claude mcp list
```

Debe aparecer cada servidor como conectado. Si falla: revisa la URL, que la
variable de entorno exista (`echo $N8N_API_KEY`) y que el token no haya caducado.
