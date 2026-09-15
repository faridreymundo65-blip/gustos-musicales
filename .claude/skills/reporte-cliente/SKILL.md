---
name: reporte-cliente
description: Genera el reporte periódico de un cliente a partir del trabajo real hecho en el repositorio y las notas del segundo cerebro. Úsala cuando pidan un reporte, un resumen semanal, un informe de avances o un entregable para un cliente.
---

# Reporte de cliente

Convierte el trabajo real en un documento que el cliente entiende. El cliente no
lee commits: lee resultados.

## 1. Reunir los hechos (no inventes ninguno)

```bash
git log --since="7 days ago" --pretty=format:'%ad %s' --date=short
git diff --stat HEAD~10..HEAD
```

Y revisa las notas del periodo:
```bash
ls -t segundo-cerebro/10-Proyectos/
```

Si un dato no sale de ahí (métricas de tráfico, ventas, resultados de campañas),
**pídeselo al usuario**. Nunca rellenes un reporte con cifras estimadas.

## 2. Estructura del reporte

Guárdalo en `segundo-cerebro/10-Proyectos/<cliente>/reportes/AAAA-MM-DD-reporte.md`:

```markdown
# <Cliente> — Reporte del <fecha inicio> al <fecha fin>

## Resumen
Dos o tres frases. Qué se consiguió esta semana, en lenguaje de negocio.

## Entregado
- <Resultado concreto> — <dónde verlo: URL o sección>

## En curso
- <Tarea> — <estado real y fecha estimada>

## Bloqueado / necesito de ti
- <Qué falta y quién lo tiene que resolver>

## Próxima semana
- <Máximo 3 prioridades>
```

## 3. Reglas de redacción

- Escribe en resultados, no en tareas: "la landing ya está online y recibe
  formularios", no "modifiqué index.html".
- Nada de jerga técnica salvo que el cliente sea técnico.
- Un bloqueo se dice claro y con dueño. Los bloqueos escondidos se convierten en
  problemas la semana siguiente.
- Máximo una página. Si no cabe, sobra texto.

## 4. Entrega

Enseña el borrador al usuario antes de enviarlo a nadie. El envío al cliente
—correo, WhatsApp, Notion— lo decide y lo aprueba siempre el usuario.
