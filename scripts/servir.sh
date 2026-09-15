#!/usr/bin/env bash
# Previsualiza el sitio en local. Uso: bash scripts/servir.sh [puerto]
set -euo pipefail

PUERTO="${1:-8000}"
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Sirviendo $RAIZ"
echo "  Sitio principal : http://localhost:$PUERTO/"
echo "  Landing Cafetal : http://localhost:$PUERTO/landing-page/"
echo "Ctrl+C para detener."

cd "$RAIZ"
python3 -m http.server "$PUERTO"
