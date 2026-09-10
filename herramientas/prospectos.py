#!/usr/bin/env python3
"""
prospectos.py - Encuentra negocios SIN sitio web y te arma la lista de contacto.

Datos de OpenStreetMap (gratis, sin API key, sin registro).

USO BASICO
    python prospectos.py lima comida
    python prospectos.py lima salud
    python prospectos.py lima todo
    python prospectos.py "Miraflores, Lima, Peru" belleza

GRUPOS DISPONIBLES (segundo argumento)
    comida      restaurantes, cafes, bares, panaderias, pollerias, juguerias...
    salud       dentistas, medicos, clinicas, farmacias, veterinarias, opticas...
    belleza     peluquerias, salones, spa, uñas, tatuajes, cosmetica...
    servicios   gasfiteros, electricistas, carpinteros, abogados, contadores,
                inmobiliarias, seguros, lavanderias, talleres, imprentas...
    tiendas     ropa, calzado, ferreteria, celulares, muebles, mascotas...
    turismo     hoteles, hostales, casas de huespedes...
    deporte     gimnasios, academias, centros deportivos...
    educacion   autoescuelas, academias, institutos, jardines...
    todo        todos los grupos juntos (tarda mas)

TAMBIEN podes pedir rubros sueltos:
    python prospectos.py lima restaurant,hairdresser,dentist

SALIDA (dos archivos, con la fecha en el nombre para no pisar los anteriores)
    prospectos_<grupo>_<fecha>.csv    -> se abre en Excel
    prospectos_<grupo>_<fecha>.html   -> se abre en el navegador, links clickeables

REQUIERE
    pip install requests
"""
import sys, csv, re, time, json, html
from datetime import datetime
from urllib.parse import quote

import requests

# --------------------------------------------------------------------------
# CONFIGURACION -- edita esto a tu gusto
# --------------------------------------------------------------------------

# Mensaje que se pre-carga en el link de WhatsApp.
# {nombre} {rubro} {distrito} se reemplazan solos.
MENSAJE = (
    "Hola {nombre}! Los encontre en Google Maps ({rubro} en {distrito}). "
    "Hago paginas web para negocios como el suyo. "
    "Les puedo mostrar una propuesta sin compromiso?"
)

NOMINATIM = "https://nominatim.openstreetmap.org/search"
OVERPASS = "https://overpass-api.de/api/interpreter"
UA = {"User-Agent": "buscador-prospectos/2.0 (uso personal)"}

LIMA = [
    "Miraflores, Lima, Peru",        "San Isidro, Lima, Peru",
    "Barranco, Lima, Peru",          "Surquillo, Lima, Peru",
    "Santiago de Surco, Lima, Peru", "San Borja, Lima, Peru",
    "Lince, Lima, Peru",             "Jesus Maria, Lima, Peru",
    "Pueblo Libre, Lima, Peru",      "Magdalena del Mar, Lima, Peru",
    "San Miguel, Lima, Peru",        "La Molina, Lima, Peru",
]

# Si el negocio tiene CUALQUIERA de estas etiquetas, ya tiene presencia online
# y lo descartamos.
TIENE_WEB = ("website", "contact:website", "url", "website:menu", "website",
             "contact:facebook", "facebook", "contact:instagram", "instagram",
             "contact:tiktok", "contact:linkedin", "contact:youtube")

# --------------------------------------------------------------------------
# QUE BUSCAR EN CADA GRUPO
# --------------------------------------------------------------------------
# Formato:  "clave_osm": [lista de valores]   o   "clave_osm": None (= todos)

GRUPOS = {
    "comida": {
        "amenity": ["restaurant", "cafe", "bar", "fast_food", "pub", "ice_cream",
                    "food_court", "biergarten", "juice_bar"],
        "shop": ["bakery", "pastry", "butcher", "confectionery", "greengrocer",
                 "seafood", "deli", "coffee", "tea", "chocolate", "cheese",
                 "beverages", "alcohol", "dairy", "health_food"],
    },
    "salud": {
        "amenity": ["dentist", "doctors", "clinic", "pharmacy", "veterinary"],
        "healthcare": None,
        "shop": ["optician", "medical_supply", "herbalist", "hearing_aids",
                 "nutrition_supplements"],
    },
    "belleza": {
        "shop": ["hairdresser", "beauty", "cosmetics", "tattoo", "massage",
                 "nail_salon", "perfumery", "hairdresser_supply"],
        "leisure": ["spa", "sauna"],
    },
    "servicios": {
        "craft": None,
        "office": None,
        "shop": ["car_repair", "laundry", "dry_cleaning", "funeral_directors",
                 "locksmith", "travel_agency", "copyshop", "photo", "tailor",
                 "shoe_repair", "car_parts", "motorcycle_repair", "printer_ink",
                 "electronics_repair", "computer_repair"],
        "amenity": ["car_wash", "car_rental", "internet_cafe"],
    },
    "tiendas": {
        "shop": ["clothes", "shoes", "jewelry", "bag", "boutique", "fabric",
                 "furniture", "hardware", "doityourself", "paint", "florist",
                 "pet", "pet_grooming", "toys", "sports", "bicycle", "books",
                 "stationery", "gift", "mobile_phone", "computer", "electronics",
                 "appliance", "houseware", "kitchen", "lighting", "garden_centre",
                 "musical_instrument", "art", "antiques", "second_hand",
                 "variety_store", "convenience", "supermarket", "kiosk",
                 "baby_goods", "watches", "optician", "curtain", "carpet"],
    },
    "turismo": {
        "tourism": ["hotel", "hostel", "guest_house", "motel", "apartment",
                    "chalet", "camp_site"],
    },
    "deporte": {
        "leisure": ["fitness_centre", "sports_centre", "dance", "horse_riding",
                    "swimming_pool", "climbing"],
    },
    "educacion": {
        "amenity": ["driving_school", "language_school", "music_school",
                    "prep_school", "kindergarten", "college", "training"],
    },
}

# --------------------------------------------------------------------------
# NOMBRES EN CASTELLANO
# --------------------------------------------------------------------------
RUBROS = {
    # comida
    "amenity=restaurant": "Restaurante", "amenity=cafe": "Cafeteria",
    "amenity=bar": "Bar", "amenity=fast_food": "Comida rapida",
    "amenity=pub": "Pub", "amenity=ice_cream": "Heladeria",
    "amenity=food_court": "Patio de comidas", "amenity=biergarten": "Cerveceria",
    "amenity=juice_bar": "Jugueria",
    "shop=bakery": "Panaderia", "shop=pastry": "Pasteleria",
    "shop=butcher": "Carniceria", "shop=confectionery": "Dulceria",
    "shop=greengrocer": "Verduleria", "shop=seafood": "Pescaderia",
    "shop=deli": "Delicatessen", "shop=coffee": "Tienda de cafe",
    "shop=tea": "Tienda de te", "shop=chocolate": "Chocolateria",
    "shop=cheese": "Queseria", "shop=beverages": "Distribuidora de bebidas",
    "shop=alcohol": "Licoreria", "shop=dairy": "Lacteos",
    "shop=health_food": "Productos naturales",
    # salud
    "amenity=dentist": "Dentista", "amenity=doctors": "Consultorio medico",
    "amenity=clinic": "Clinica", "amenity=pharmacy": "Farmacia",
    "amenity=veterinary": "Veterinaria",
    "healthcare=physiotherapist": "Fisioterapia",
    "healthcare=psychotherapist": "Psicologia",
    "healthcare=laboratory": "Laboratorio", "healthcare=dentist": "Dentista",
    "healthcare=doctor": "Consultorio medico", "healthcare=centre": "Centro de salud",
    "healthcare=alternative": "Medicina alternativa",
    "healthcare=optometrist": "Optometria", "healthcare=podiatrist": "Podologia",
    "healthcare=nutrition_counselling": "Nutricionista",
    "healthcare=speech_therapist": "Fonoaudiologia",
    "healthcare=midwife": "Obstetricia", "healthcare=birthing_centre": "Centro de partos",
    "healthcare=rehabilitation": "Rehabilitacion",
    "shop=optician": "Optica", "shop=medical_supply": "Insumos medicos",
    "shop=herbalist": "Herboristeria", "shop=hearing_aids": "Audifonos",
    "shop=nutrition_supplements": "Suplementos",
    # belleza
    "shop=hairdresser": "Peluqueria", "shop=beauty": "Salon de belleza",
    "shop=cosmetics": "Cosmetica", "shop=tattoo": "Tatuajes",
    "shop=massage": "Masajes", "shop=nail_salon": "Salon de uñas",
    "shop=perfumery": "Perfumeria", "shop=hairdresser_supply": "Insumos de peluqueria",
    "leisure=spa": "Spa", "leisure=sauna": "Sauna",
    # servicios - craft
    "craft=carpenter": "Carpinteria", "craft=electrician": "Electricista",
    "craft=plumber": "Gasfitero", "craft=painter": "Pintor",
    "craft=shoemaker": "Zapateria", "craft=tailor": "Sastreria",
    "craft=photographer": "Fotografo", "craft=locksmith": "Cerrajeria",
    "craft=metal_construction": "Metalmecanica", "craft=upholsterer": "Tapiceria",
    "craft=jeweller": "Joyeria", "craft=window_construction": "Ventaneria",
    "craft=key_cutter": "Duplicado de llaves", "craft=blacksmith": "Herreria",
    "craft=glaziery": "Vidrieria", "craft=confectionery": "Reposteria",
    "craft=gardener": "Jardineria", "craft=builder": "Constructor",
    "craft=hvac": "Aire acondicionado", "craft=sawmill": "Aserradero",
    "craft=dressmaker": "Modista", "craft=signmaker": "Letreros",
    "craft=printer": "Imprenta", "craft=caterer": "Catering",
    # servicios - office
    "office=lawyer": "Abogado", "office=accountant": "Contador",
    "office=estate_agent": "Inmobiliaria", "office=insurance": "Seguros",
    "office=architect": "Arquitecto", "office=travel_agent": "Agencia de viajes",
    "office=advertising_agency": "Agencia de publicidad", "office=it": "Empresa de TI",
    "office=employment_agency": "Bolsa de trabajo", "office=company": "Empresa",
    "office=financial": "Financiera", "office=educational_institution": "Instituto",
    "office=engineer": "Ingenieria", "office=notary": "Notaria",
    "office=tax_advisor": "Asesor tributario", "office=logistics": "Logistica",
    "office=association": "Asociacion", "office=coworking": "Coworking",
    "office=telecommunication": "Telecomunicaciones", "office=surveyor": "Topografia",
    "office=consulting": "Consultora", "office=marketing": "Marketing",
    # servicios - shop / amenity
    "shop=car_repair": "Taller mecanico", "shop=laundry": "Lavanderia",
    "shop=dry_cleaning": "Tintoreria", "shop=funeral_directors": "Funeraria",
    "shop=locksmith": "Cerrajeria", "shop=travel_agency": "Agencia de viajes",
    "shop=copyshop": "Copias e impresiones", "shop=photo": "Estudio fotografico",
    "shop=tailor": "Sastreria", "shop=shoe_repair": "Reparacion de calzado",
    "shop=car_parts": "Repuestos", "shop=motorcycle_repair": "Taller de motos",
    "shop=printer_ink": "Tintas y toners",
    "shop=electronics_repair": "Reparacion de electronica",
    "shop=computer_repair": "Reparacion de PC",
    "amenity=car_wash": "Lavado de autos", "amenity=car_rental": "Alquiler de autos",
    "amenity=internet_cafe": "Cabinas de internet",
    # tiendas
    "shop=clothes": "Ropa", "shop=shoes": "Calzado", "shop=jewelry": "Joyeria",
    "shop=bag": "Carteras y maletas", "shop=boutique": "Boutique",
    "shop=fabric": "Telas", "shop=furniture": "Muebleria",
    "shop=hardware": "Ferreteria", "shop=doityourself": "Ferreteria / hogar",
    "shop=paint": "Pinturas", "shop=florist": "Floreria",
    "shop=pet": "Tienda de mascotas", "shop=pet_grooming": "Peluqueria canina",
    "shop=toys": "Jugueteria", "shop=sports": "Articulos deportivos",
    "shop=bicycle": "Bicicleteria", "shop=books": "Libreria",
    "shop=stationery": "Libreria / utiles", "shop=gift": "Regaleria",
    "shop=mobile_phone": "Celulares", "shop=computer": "Computacion",
    "shop=electronics": "Electronica", "shop=appliance": "Electrodomesticos",
    "shop=houseware": "Bazar", "shop=kitchen": "Cocinas",
    "shop=lighting": "Iluminacion", "shop=garden_centre": "Vivero",
    "shop=musical_instrument": "Instrumentos musicales", "shop=art": "Galeria de arte",
    "shop=antiques": "Antiguedades", "shop=second_hand": "Segunda mano",
    "shop=variety_store": "Bazar", "shop=convenience": "Minimarket",
    "shop=supermarket": "Supermercado", "shop=kiosk": "Kiosco",
    "shop=baby_goods": "Articulos de bebe", "shop=watches": "Relojeria",
    "shop=curtain": "Cortinas", "shop=carpet": "Alfombras",
    # turismo
    "tourism=hotel": "Hotel", "tourism=hostel": "Hostal",
    "tourism=guest_house": "Casa de huespedes", "tourism=motel": "Motel",
    "tourism=apartment": "Departamento turistico", "tourism=chalet": "Cabaña",
    "tourism=camp_site": "Camping",
    # deporte
    "leisure=fitness_centre": "Gimnasio", "leisure=sports_centre": "Centro deportivo",
    "leisure=dance": "Academia de baile", "leisure=horse_riding": "Equitacion",
    "leisure=swimming_pool": "Piscina", "leisure=climbing": "Escalada",
    # educacion
    "amenity=driving_school": "Autoescuela", "amenity=language_school": "Academia de idiomas",
    "amenity=music_school": "Academia de musica", "amenity=prep_school": "Academia preuniversitaria",
    "amenity=kindergarten": "Jardin de infantes", "amenity=college": "Instituto",
    "amenity=training": "Centro de capacitacion",
}

COCINA = {
    "peruvian": "Peruana", "chicken": "Pollos", "pizza": "Pizzeria",
    "chinese": "Chifa", "japanese": "Japonesa", "sushi": "Sushi",
    "seafood": "Cevicheria / mariscos", "italian": "Italiana",
    "burger": "Hamburguesas", "sandwich": "Sandwiches", "mexican": "Mexicana",
    "regional": "Comida criolla", "international": "Internacional",
    "coffee_shop": "Cafeteria", "barbecue": "Parrilla", "steak_house": "Parrilla",
    "vegetarian": "Vegetariana", "vegan": "Vegana", "asian": "Asiatica",
    "thai": "Tailandesa", "indian": "India", "arab": "Arabe", "korean": "Coreana",
    "american": "Americana", "spanish": "Española", "french": "Francesa",
    "breakfast": "Desayunos", "juice": "Jugueria", "fish": "Pescados",
    "ice_cream": "Helados", "cake": "Tortas", "dessert": "Postres",
    "noodle": "Fideos", "soup": "Sopas", "empanada": "Empanadas",
    "friture": "Frituras", "grill": "Parrilla", "local": "Comida local",
    "latin_american": "Latinoamericana", "criollo": "Criolla",
}

# Campos que ya extraemos en columnas propias: no se repiten en "otros_datos"
YA_USADOS = {
    "name", "amenity", "shop", "craft", "office", "healthcare", "tourism",
    "leisure", "cuisine", "phone", "contact:phone", "mobile", "contact:mobile",
    "whatsapp", "contact:whatsapp", "email", "contact:email",
    "addr:street", "addr:housenumber", "addr:suburb", "addr:neighbourhood",
    "addr:city", "addr:district", "opening_hours", "delivery", "takeaway",
    "outdoor_seating", "capacity", "wheelchair", "air_conditioning",
    "internet_access", "diet:vegetarian", "diet:vegan", "operator", "brand",
    "brand:wikidata", "description", "check_date", "reservation", "smoking",
    "source", "source:date", "created_by", "note", "fixme",
}


# --------------------------------------------------------------------------
# UTILIDADES
# --------------------------------------------------------------------------
def limpiar_tel(crudo):
    """Normaliza un telefono peruano -> (numero_e164, es_celular)."""
    if not crudo:
        return "", False
    # OSM a veces guarda varios numeros en el mismo campo: nos quedamos con el primero
    crudo = re.split(r"[;,/]", crudo)[0]
    d = re.sub(r"\D", "", crudo)
    d = d.lstrip("0")
    if d.startswith("51") and len(d) > 9:
        d = d[2:]
    d = d.lstrip("0")

    if len(d) == 9 and d.startswith("9"):      # celular -> tiene WhatsApp
        return "51" + d, True
    if len(d) == 7:                            # fijo Lima sin codigo
        return "511" + d, False
    if len(d) == 8 and d.startswith("1"):      # fijo Lima con codigo
        return "51" + d, False
    if len(d) >= 8:
        return "51" + d, False
    return "", False


def todos_los_telefonos(tags):
    """Junta y normaliza todos los telefonos del negocio."""
    crudos = []
    for k in ("contact:whatsapp", "whatsapp", "contact:mobile", "mobile",
              "phone", "contact:phone"):
        v = tags.get(k, "")
        if v:
            crudos += [p.strip() for p in re.split(r"[;,/]", v) if p.strip()]

    vistos, nums = set(), []
    for c in crudos:
        num, cel = limpiar_tel(c)
        if num and num not in vistos:
            vistos.add(num)
            nums.append((num, cel))
    return nums


def traducir_cocina(tags):
    c = tags.get("cuisine", "")
    if not c:
        return ""
    return " / ".join(COCINA.get(p.strip(), p.strip().replace("_", " ").title())
                      for p in c.split(";"))


def rubro_de(tags):
    """Devuelve (clave=valor, nombre en castellano)."""
    for k in ("amenity", "shop", "craft", "office", "healthcare",
              "tourism", "leisure"):
        v = tags.get(k)
        if v:
            crudo = f"{k}={v}"
            return crudo, RUBROS.get(crudo, v.replace("_", " ").capitalize())
    return "", ""


def medios_de_pago(tags):
    acepta = [k.split(":", 1)[1].replace("_", " ")
              for k, v in tags.items()
              if k.startswith("payment:") and v in ("yes", "only")]
    return ", ".join(sorted(acepta))


# --------------------------------------------------------------------------
# CONSULTAS A OPENSTREETMAP
# --------------------------------------------------------------------------
def area_id(zona):
    r = requests.get(NOMINATIM, params={"q": zona, "format": "json", "limit": 1},
                     headers=UA, timeout=30)
    r.raise_for_status()
    res = r.json()
    if not res:
        print(f"  !! no encontrado: {zona}")
        return None
    d = res[0]
    if d["osm_type"] != "relation":
        print(f"  !! '{zona}' no es un area en OSM")
        return None
    return 3600000000 + int(d["osm_id"])


def buscar(aid, seleccion, intentos=3):
    partes = []
    for clave, valores in seleccion.items():
        if valores is None:
            partes.append(f'  nwr["{clave}"]["name"](area.a);')
        else:
            alt = "|".join(valores)
            partes.append(f'  nwr["{clave}"~"^({alt})$"]["name"](area.a);')

    q = ("[out:json][timeout:300];\narea({})->.a;\n(\n{}\n);\nout center tags;\n"
         .format(aid, "\n".join(partes)))

    for intento in range(1, intentos + 1):
        try:
            r = requests.post(OVERPASS, data={"data": q}, headers=UA, timeout=300)
            r.raise_for_status()
            return r.json()["elements"]
        except Exception as e:
            if intento == intentos:
                raise
            espera = 15 * intento
            print(f"(reintento {intento}, {e.__class__.__name__}, espero {espera}s)",
                  end=" ", flush=True)
            time.sleep(espera)
    return []


# --------------------------------------------------------------------------
# ARMADO DE LA FILA
# --------------------------------------------------------------------------
def armar_fila(e, distrito, grupo):
    tags = e.get("tags", {})

    lat = e.get("lat") or e.get("center", {}).get("lat")
    lon = e.get("lon") or e.get("center", {}).get("lon")

    nombre = tags.get("name", "")
    rubro_crudo, rubro = rubro_de(tags)

    nums = todos_los_telefonos(tags)
    principal, es_cel = (nums[0] if nums else ("", False))
    confirmado = bool(tags.get("contact:whatsapp") or tags.get("whatsapp"))
    # si no hay whatsapp explicito, preferimos un celular sobre un fijo
    if nums and not es_cel:
        for n, c in nums:
            if c:
                principal, es_cel = n, c
                break

    direccion = " ".join(filter(None, [tags.get("addr:street", ""),
                                       tags.get("addr:housenumber", "")]))
    barrio = tags.get("addr:suburb") or tags.get("addr:neighbourhood", "")
    marca = tags.get("brand", "")
    es_cadena = bool(marca or tags.get("brand:wikidata"))

    wa_link = ""
    if principal and (es_cel or confirmado):
        texto = MENSAJE.format(nombre=nombre, rubro=rubro.lower(), distrito=distrito)
        wa_link = f"https://wa.me/{principal}?text={quote(texto)}"

    # ---- puntaje y motivo ----
    score, motivos = 0, []
    if confirmado:
        score += 4; motivos.append("WhatsApp confirmado")
    elif es_cel:
        score += 3; motivos.append("celular (WhatsApp probable)")
    elif principal:
        score += 1; motivos.append("solo telefono fijo")
    else:
        motivos.append("sin telefono")

    if direccion:
        score += 1; motivos.append("con direccion")
    if tags.get("opening_hours"):
        score += 1; motivos.append("con horario")
    if tags.get("email") or tags.get("contact:email"):
        score += 1; motivos.append("con email")
    if tags.get("cuisine") or tags.get("description"):
        score += 1
    if es_cadena:
        score -= 3; motivos.append("OJO: parece cadena/franquicia")

    otros = {k: v for k, v in tags.items()
             if k not in YA_USADOS and not k.startswith("payment:")}

    return {
        "prioridad": score,
        "motivo": "; ".join(motivos),
        "distrito": distrito,
        "nombre": nombre,
        "rubro": rubro,
        "grupo": grupo,
        "especialidad": traducir_cocina(tags) or tags.get("description", "")[:80],
        "whatsapp": wa_link,
        "wa_confirmado": "si" if confirmado else ("probable" if es_cel else ""),
        "telefono": f"+{principal}" if principal else "",
        "tipo_linea": "celular" if es_cel else ("fijo" if principal else ""),
        "telefonos_todos": " | ".join(f"+{n}" for n, _ in nums),
        "email": tags.get("email") or tags.get("contact:email", ""),
        "direccion": direccion,
        "barrio": barrio,
        "ciudad": tags.get("addr:city", ""),
        "horario": tags.get("opening_hours", ""),
        "delivery": tags.get("delivery", ""),
        "para_llevar": tags.get("takeaway", ""),
        "reservas": tags.get("reservation", ""),
        "terraza": tags.get("outdoor_seating", ""),
        "capacidad": tags.get("capacity", ""),
        "vegetariano": tags.get("diet:vegetarian", ""),
        "vegano": tags.get("diet:vegan", ""),
        "acceso_silla": tags.get("wheelchair", ""),
        "aire_acondicionado": tags.get("air_conditioning", ""),
        "wifi": tags.get("internet_access", ""),
        "pagos": medios_de_pago(tags),
        "operador": tags.get("operator", ""),
        "marca": marca,
        "es_cadena": "si" if es_cadena else "",
        "descripcion": tags.get("description", ""),
        "rubro_osm": rubro_crudo,
        "ultima_revision": tags.get("check_date", ""),
        "lat": lat,
        "lon": lon,
        "maps": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}",
        "osm": f"https://www.openstreetmap.org/{e['type']}/{e['id']}",
        "otros_datos": json.dumps(otros, ensure_ascii=False) if otros else "",
    }


# --------------------------------------------------------------------------
# REPORTE HTML
# --------------------------------------------------------------------------
def escribir_html(filas, ruta, titulo, resumen):
    def celda(f):
        wa = (f'<a class="wa" href="{html.escape(f["whatsapp"])}" target="_blank">WhatsApp</a>'
              if f["whatsapp"] else '<span class="no">-</span>')
        tel = html.escape(f["telefono"]) or "-"
        return f"""<tr>
<td class="p p{max(0, min(8, f['prioridad']))}">{f['prioridad']}</td>
<td><strong>{html.escape(f['nombre'])}</strong>
    <div class="sub">{html.escape(f['especialidad'])}</div></td>
<td>{html.escape(f['rubro'])}</td>
<td>{html.escape(f['distrito'])}</td>
<td>{wa}<div class="sub">{tel}</div></td>
<td>{html.escape(f['direccion'])}<div class="sub">{html.escape(f['horario'])}</div></td>
<td><a href="{html.escape(f['maps'])}" target="_blank">Maps</a></td>
</tr>"""

    cuerpo = "\n".join(celda(f) for f in filas)
    doc = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(titulo)}</title>
<style>
 body{{font:14px system-ui,sans-serif;margin:0;padding:24px;background:#f6f7f9;color:#1a1a1a}}
 h1{{font-size:20px;margin:0 0 4px}}
 .resumen{{color:#555;margin-bottom:16px;white-space:pre-line}}
 #q{{width:100%;max-width:420px;padding:10px 12px;font-size:15px;border:1px solid #ccc;
     border-radius:8px;margin-bottom:14px}}
 table{{width:100%;border-collapse:collapse;background:#fff;border-radius:10px;overflow:hidden;
        box-shadow:0 1px 3px rgba(0,0,0,.1)}}
 th,td{{padding:9px 11px;text-align:left;border-bottom:1px solid #eee;vertical-align:top}}
 th{{background:#eceff3;font-size:12px;text-transform:uppercase;letter-spacing:.4px}}
 tr:hover td{{background:#fafbfc}}
 .sub{{color:#777;font-size:12px;margin-top:2px}}
 .wa{{background:#25d366;color:#fff;padding:4px 10px;border-radius:6px;
      text-decoration:none;font-weight:600;font-size:12px;display:inline-block}}
 .no{{color:#bbb}}
 a{{color:#0b62d0}}
 .p{{font-weight:700;text-align:center;width:38px}}
 .p7,.p8{{background:#d6f5dd}} .p5,.p6{{background:#eaf7d6}}
 .p3,.p4{{background:#fdf3d0}} .p0,.p1,.p2{{background:#f5f5f5;color:#999}}
</style></head><body>
<h1>{html.escape(titulo)}</h1>
<div class="resumen">{html.escape(resumen)}</div>
<input id="q" placeholder="Filtrar por nombre, rubro o distrito...">
<table><thead><tr>
<th>Pri</th><th>Negocio</th><th>Rubro</th><th>Distrito</th>
<th>Contacto</th><th>Direccion / horario</th><th>Mapa</th>
</tr></thead><tbody id="t">
{cuerpo}
</tbody></table>
<script>
 const q=document.getElementById('q'),f=[...document.querySelectorAll('#t tr')];
 q.addEventListener('input',()=>{{const v=q.value.toLowerCase();
   f.forEach(r=>r.style.display=r.textContent.toLowerCase().includes(v)?'':'none');}});
</script></body></html>"""
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(doc)


# --------------------------------------------------------------------------
# PRINCIPAL
# --------------------------------------------------------------------------
def resolver_seleccion(pedido):
    """Convierte el argumento del usuario en {clave_osm: [valores]}."""
    # indice valor -> clave, armado desde la tabla de rubros
    indice = {}
    for crudo in RUBROS:
        k, v = crudo.split("=", 1)
        indice.setdefault(v, k)

    seleccion, grupos = {}, []
    for token in [t.strip() for t in pedido.split(",") if t.strip()]:
        if token == "todo":
            grupos = list(GRUPOS)
            for g in GRUPOS.values():
                for k, vs in g.items():
                    if vs is None:
                        seleccion[k] = None
                    elif seleccion.get(k, []) is not None:
                        seleccion[k] = sorted(set(seleccion.get(k, []) or []) | set(vs))
        elif token in GRUPOS:
            grupos.append(token)
            for k, vs in GRUPOS[token].items():
                if vs is None:
                    seleccion[k] = None
                elif seleccion.get(k, []) is not None:
                    seleccion[k] = sorted(set(seleccion.get(k, []) or []) | set(vs))
        elif "=" in token:
            k, v = token.split("=", 1)
            if seleccion.get(k, []) is not None:
                seleccion[k] = sorted(set(seleccion.get(k, []) or []) | {v})
            grupos.append(v)
        elif token in indice:
            k = indice[token]
            if seleccion.get(k, []) is not None:
                seleccion[k] = sorted(set(seleccion.get(k, []) or []) | {token})
            grupos.append(token)
        else:
            print(f"  !! rubro desconocido, lo salto: {token}")
    return seleccion, grupos


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)

    arg = sys.argv[1]
    zonas = LIMA if arg.lower() == "lima" else [z.strip() for z in arg.split(";")]
    pedido = sys.argv[2] if len(sys.argv) > 2 else "comida"

    seleccion, grupos = resolver_seleccion(pedido)
    if not seleccion:
        sys.exit("No entendi que rubros buscar. Mira la ayuda arriba.")

    etiqueta = "-".join(dict.fromkeys(grupos))[:40] or "rubros"
    print(f"\nBuscando: {', '.join(dict.fromkeys(grupos))}")
    print(f"Zonas   : {len(zonas)}\n")

    filas, vistos = [], set()
    bruto = conweb = 0

    for i, zona in enumerate(zonas, 1):
        distrito = zona.split(",")[0]
        print(f"[{i}/{len(zonas)}] {distrito} ...", end=" ", flush=True)

        try:
            aid = area_id(zona)
        except Exception as e:
            print(f"error buscando el area ({e.__class__.__name__}), salta")
            continue
        if aid is None:
            continue
        time.sleep(1.2)

        try:
            elems = buscar(aid, seleccion)
        except Exception as e:
            print(f"fallo ({e.__class__.__name__}), salta")
            time.sleep(10)
            continue

        nuevos = 0
        for e in elems:
            tags = e.get("tags", {})
            bruto += 1
            if any(tags.get(k) for k in TIENE_WEB):
                conweb += 1
                continue
            clave = (e["type"], e["id"])
            if clave in vistos:
                continue
            vistos.add(clave)
            nuevos += 1
            filas.append(armar_fila(e, distrito, etiqueta))

        print(f"{len(elems)} hallados, {nuevos} sin web")
        time.sleep(2)

    if not filas:
        sys.exit("\nNo salio nada. Revisa el nombre de la zona o intenta mas tarde.")

    filas.sort(key=lambda x: (-x["prioridad"], x["distrito"], x["nombre"]))

    fecha = datetime.now().strftime("%Y-%m-%d_%H%M")
    base = f"prospectos_{etiqueta}_{fecha}"

    with open(base + ".csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)

    con_wa = sum(1 for x in filas if x["whatsapp"])
    conf = sum(1 for x in filas if x["wa_confirmado"] == "si")
    con_tel = sum(1 for x in filas if x["telefono"])
    con_mail = sum(1 for x in filas if x["email"])
    cadenas = sum(1 for x in filas if x["es_cadena"])

    resumen = (
        f"Revisados: {bruto}   |   Ya tienen web o redes: {conweb}\n"
        f"SIN presencia online: {len(filas)}\n"
        f"Con telefono: {con_tel}   |   Con WhatsApp: {con_wa} "
        f"({conf} confirmados, {con_wa - conf} probables)   |   Con email: {con_mail}\n"
        f"Marcados como cadena/franquicia: {cadenas}"
    )

    escribir_html(filas, base + ".html",
                  f"Prospectos sin web - {etiqueta}", resumen)

    print("\n" + "=" * 70)
    print(resumen)
    print("=" * 70)
    print(f"\nArchivos generados en esta carpeta:")
    print(f"  {base}.csv    <- abrilo en Excel")
    print(f"  {base}.html   <- abrilo en el navegador (links clickeables)\n")

    contactables = [x for x in filas if x["whatsapp"]]
    if contactables:
        print(f"TOP {min(15, len(contactables))} PARA CONTACTAR HOY\n")
        for x in contactables[:15]:
            print(f"  [{x['prioridad']}] {x['nombre'][:34]:<36} "
                  f"{x['rubro'][:18]:<20} {x['distrito']}")
            print(f"      {x['telefono']}  ({x['wa_confirmado']})")
            if x["direccion"]:
                print(f"      {x['direccion']}")
            print()
    else:
        print("Ninguno tiene celular cargado en OSM. Usa la columna 'maps' del CSV\n"
              "para buscar el telefono en Google Maps.\n")


if __name__ == "__main__":
    main()
