# prospectos.py

Encuentra negocios **sin sitio web** en OpenStreetMap y arma la lista de contacto
(con links de WhatsApp pre-escritos) para ofrecerles hacerles una.

Datos de OpenStreetMap: gratis, sin API key, sin registro.

## Instalacion

```bash
pip install requests
```

## Uso

```bash
python prospectos.py lima comida
python prospectos.py lima salud
python prospectos.py lima todo
python prospectos.py "Miraflores, Lima, Peru" belleza
python prospectos.py lima restaurant,hairdresser,dentist
```

Primer argumento: `lima` (12 distritos) o el nombre de una zona.
Segundo argumento: un grupo, o rubros sueltos separados por coma.

### Grupos

| Grupo | Incluye |
|---|---|
| `comida` | restaurantes, cafes, bares, panaderias, juguerias, licorerias... |
| `salud` | dentistas, medicos, clinicas, farmacias, veterinarias, opticas... |
| `belleza` | peluquerias, salones, spa, uñas, tatuajes, cosmetica... |
| `servicios` | gasfiteros, electricistas, abogados, contadores, inmobiliarias, talleres... |
| `tiendas` | ropa, calzado, ferreteria, celulares, muebles, mascotas... |
| `turismo` | hoteles, hostales, casas de huespedes... |
| `deporte` | gimnasios, academias de baile, centros deportivos... |
| `educacion` | autoescuelas, academias, institutos, jardines... |
| `todo` | todos los grupos juntos (tarda mas) |

## Salida

Dos archivos con la fecha en el nombre (no pisa los anteriores):

- `prospectos_<grupo>_<fecha>.csv` — 39 columnas, se abre en Excel
- `prospectos_<grupo>_<fecha>.html` — reporte con buscador y links clickeables

## Como funciona

1. **Nominatim** convierte el nombre de la zona en un area de OSM.
2. **Overpass** trae los negocios de esos rubros dentro del area.
3. Se descarta todo el que tenga `website`, `facebook`, `instagram`, etc.
4. Se normalizan los telefonos al formato peruano: 9 digitos que empiezan
   en 9 = celular = probablemente tiene WhatsApp.
5. Se puntua cada prospecto y se ordena de mejor a peor.

## Limitaciones (importantes)

- **OSM esta incompleto en Peru.** La mayoria de los negocios estan mapeados
  solo con nombre y ubicacion. Espera que ~5% tenga celular cargado.
  Para el resto, usa la columna `maps` y busca el telefono en Google Maps.
- **"Sin web" es segun OSM.** El negocio puede tener pagina y nadie la cargo ahi.
  Verifica en Google antes de contactar.
- **`wa_confirmado` = `probable`** significa que es un celular, no que el
  WhatsApp este confirmado.
- Overpass es un servidor gratuito y compartido: si falla, el script reintenta
  3 veces y sigue. Intenta mas tarde si se cae seguido.

## Configuracion

El mensaje de WhatsApp se edita en la constante `MENSAJE`, arriba de todo.
Los distritos de Lima, en la lista `LIMA`.
