# -*- coding: utf-8 -*-
"""
===============================================================================
 SISTEMA DE GESTION DE INVENTARIO Y REGISTRO DE VENTAS PARA UNA MICROEMPRESA
 Aplicacion de consola desarrollada en Python 3
===============================================================================
 Curso      : PIAD-221 - Algoritmos y Programacion para Desarrollo de Software
 Carrera    : Tecnologias de la Informacion
 Trabajo    : Trabajo Final de Curso
 Caso       : Tienda de accesorios tecnologicos "TecnoStore"
 Estudiante : [COLOCAR NOMBRES Y APELLIDOS]
 ID         : [COLOCAR ID / CODIGO DE MATRICULA]
 Instructor : [COLOCAR NOMBRE DEL INSTRUCTOR]
 Fecha      : [COLOCAR FECHA DE ENTREGA]
-------------------------------------------------------------------------------
 DESCRIPCION GENERAL
-------------------------------------------------------------------------------
 Aplicacion de consola que automatiza el registro, consulta y actualizacion de
 productos del inventario, asi como el procesamiento de transacciones de venta
 de una microempresa dedicada a la comercializacion de accesorios tecnologicos.

 La solucion sustituye el registro manual en cuadernos y hojas de calculo
 desconectadas, eliminando la desactualizacion del stock, los errores humanos
 de calculo y la perdida de tiempo en la busqueda de productos.

-------------------------------------------------------------------------------
 ARQUITECTURA MODULAR (5 capas, sin programacion lineal ni monolitica)
-------------------------------------------------------------------------------
   CAPA 1 - CONFIGURACION .... Constantes globales del sistema.
   CAPA 2 - PERSISTENCIA ..... Lectura/escritura en archivos de texto plano
                               con la sentencia "with" y los modos r, w, a.
   CAPA 3 - VALIDACION ....... Entrada segura de datos con try-except-else-finally.
   CAPA 4 - LOGICA DE NEGOCIO  Reglas del negocio; NO usa print() ni input().
   CAPA 5 - INTERFAZ / CONTROL Presentacion en consola y menu principal.

 Regla de separacion de responsabilidades: la CAPA 4 (logica de negocio) es
 completamente independiente de la consola; recibe parametros y devuelve
 valores de retorno, por lo que puede reutilizarse en una futura interfaz
 grafica o web sin modificar una sola linea.

-------------------------------------------------------------------------------
 ARCHIVOS DE DATOS GENERADOS (persistencia entre ejecuciones)
-------------------------------------------------------------------------------
   datos/inventario.txt ... Catalogo de productos (se reescribe con modo "w").
   datos/ventas.txt ....... Historial de ventas (se agrega con modo "a").
   datos/errores.log ...... Bitacora de excepciones (se agrega con modo "a").

-------------------------------------------------------------------------------
 EJECUCION
-------------------------------------------------------------------------------
   python sistema_inventario.py
===============================================================================
"""

import os
import sys
from datetime import datetime

# =============================================================================
# CAPA 1: CONFIGURACION - CONSTANTES GLOBALES
# -----------------------------------------------------------------------------
# Las constantes se declaran en el ambito GLOBAL (accesibles desde cualquier
# funcion en modo lectura). Las variables de trabajo, en cambio, son LOCALES y
# viajan entre funciones como parametros y valores de retorno.
# =============================================================================

NOMBRE_EMPRESA = "TECNOSTORE E.I.R.L."
RUBRO_EMPRESA = "Venta de accesorios tecnologicos"

CARPETA_DATOS = "datos"                                 # Carpeta de persistencia
ARCHIVO_INVENTARIO = os.path.join(CARPETA_DATOS, "inventario.txt")
ARCHIVO_VENTAS = os.path.join(CARPETA_DATOS, "ventas.txt")
ARCHIVO_LOG = os.path.join(CARPETA_DATOS, "errores.log")

SEPARADOR_CAMPO = ";"          # Separa los campos de un registro
SEPARADOR_ITEM = "|"           # Separa los items dentro de una venta
SEPARADOR_SUBCAMPO = ":"       # Separa los datos dentro de un item

IGV = 0.18                     # Impuesto General a las Ventas (18%)
STOCK_MINIMO = 5               # Umbral de alerta de stock critico
ANCHO = 78                     # Ancho estandar de la consola

# Reglas de descuento por volumen: (cantidad minima, porcentaje de descuento)
ESCALA_DESCUENTOS = [(12, 12.0), (6, 8.0), (3, 5.0)]

CATEGORIAS = ["Audio", "Computo", "Conectividad", "Energia", "Accesorios"]

# Opciones validas del menu principal (se usan para validar la navegacion)
OPCIONES_MENU = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


# =============================================================================
# CAPA 2: PERSISTENCIA DE DATOS
# -----------------------------------------------------------------------------
# Toda la entrada/salida a disco se concentra aqui. Se utiliza EXCLUSIVAMENTE
# archivos de texto plano manejados con la sentencia "with" (context manager),
# que garantiza el cierre automatico del archivo incluso si ocurre un error.
#
#   Modo "r" -> leer el catalogo y el historial al iniciar el programa.
#   Modo "w" -> reescribir por completo el inventario actualizado.
#   Modo "a" -> agregar (append) una venta o un error sin borrar lo anterior.
# =============================================================================

def registrar_error(origen, detalle):
    """Escribe una excepcion en la bitacora datos/errores.log (modo "a").

    Parametros:
        origen  (str): nombre de la funcion donde ocurrio el error.
        detalle (str): descripcion tecnica de la excepcion capturada.
    Retorna:
        bool: True si el error pudo registrarse en la bitacora.
    """
    try:
        os.makedirs(CARPETA_DATOS, exist_ok=True)
        marca = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(ARCHIVO_LOG, "a", encoding="utf-8") as bitacora:
            bitacora.write("[{0}] {1} -> {2}\n".format(marca, origen, detalle))
    except OSError:
        # Si ni siquiera se puede escribir la bitacora, el programa NO se detiene.
        return False
    else:
        return True


def inicializar_almacenamiento():
    """Crea la carpeta y los archivos de datos si aun no existen.

    Se ejecuta una sola vez al arrancar el sistema. Utiliza el modo "a", que
    crea el archivo cuando no existe y no destruye la informacion si ya existe.

    Retorna:
        bool: True si el almacenamiento quedo listo para usarse.
    """
    listo = False
    try:
        os.makedirs(CARPETA_DATOS, exist_ok=True)
        for ruta in (ARCHIVO_INVENTARIO, ARCHIVO_VENTAS, ARCHIVO_LOG):
            with open(ruta, "a", encoding="utf-8"):
                pass  # Solo se asegura la existencia fisica del archivo.
    except PermissionError as error:
        print("  [!] Sin permisos de escritura en la carpeta de datos:", error)
        registrar_error("inicializar_almacenamiento", str(error))
    except OSError as error:
        print("  [!] No fue posible preparar el almacenamiento:", error)
        registrar_error("inicializar_almacenamiento", str(error))
    else:
        listo = True
    finally:
        # El bloque finally SIEMPRE se ejecuta: confirme o no la operacion.
        print("  [OK] Verificacion del almacenamiento finalizada.")
    return listo


def linea_a_producto(linea):
    """Convierte una linea del archivo de texto en un diccionario producto.

    Formato del registro: id;nombre;categoria;precio;stock

    Parametros:
        linea (str): linea leida del archivo inventario.txt.
    Retorna:
        dict: producto estructurado.
    Lanza:
        ValueError: si el registro esta incompleto o mal formado.
    """
    campos = linea.strip().split(SEPARADOR_CAMPO)
    if len(campos) != 5:
        raise ValueError("El registro no tiene los 5 campos requeridos")

    producto = {
        "id": campos[0].strip().upper(),
        "nombre": campos[1].strip(),
        "categoria": campos[2].strip(),
        "precio": float(campos[3]),     # Puede lanzar ValueError
        "stock": int(campos[4]),        # Puede lanzar ValueError
    }
    if producto["precio"] < 0 or producto["stock"] < 0:
        raise ValueError("El precio y el stock no pueden ser negativos")
    return producto


def producto_a_linea(producto):
    """Convierte un diccionario producto en una linea de texto grabable.

    Parametros:
        producto (dict): producto del inventario.
    Retorna:
        str: linea con el formato id;nombre;categoria;precio;stock
    """
    return "{0};{1};{2};{3:.2f};{4}\n".format(
        producto["id"], producto["nombre"], producto["categoria"],
        producto["precio"], producto["stock"])


def cargar_inventario(ruta=ARCHIVO_INVENTARIO):
    """Carga el catalogo de productos desde el archivo de texto (modo "r").

    Los registros corruptos NO detienen la carga: se informan, se registran en
    la bitacora y el proceso continua con el resto de lineas (continue).

    Parametros:
        ruta (str): ubicacion del archivo de inventario.
    Retorna:
        list: lista de diccionarios con los productos cargados.
    """
    inventario = []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()          # Metodo read()
    except FileNotFoundError:
        print("  [!] No se encontro '{0}'. Se iniciara un inventario vacio.".format(ruta))
        registrar_error("cargar_inventario", "FileNotFoundError: " + ruta)
    except PermissionError as error:
        print("  [!] Archivo de inventario bloqueado por el sistema:", error)
        registrar_error("cargar_inventario", str(error))
    except UnicodeDecodeError as error:
        print("  [!] El archivo de inventario tiene una codificacion invalida.")
        registrar_error("cargar_inventario", str(error))
    else:
        numero = 0
        for linea in contenido.splitlines():
            numero += 1
            if not linea.strip():
                continue                        # Ignora lineas en blanco
            try:
                producto = linea_a_producto(linea)
            except ValueError as error:
                print("  [!] Linea {0} descartada del inventario ({1}).".format(numero, error))
                registrar_error("cargar_inventario", "Linea {0}: {1}".format(numero, error))
                continue                        # El programa NO se interrumpe
            inventario.append(producto)
        print("  [OK] Inventario cargado: {0} producto(s).".format(len(inventario)))
    finally:
        print("  [i] Proceso de lectura del inventario finalizado.")
    return inventario


def guardar_inventario(inventario, ruta=ARCHIVO_INVENTARIO):
    """Graba TODO el inventario en el archivo de texto (modo "w").

    El modo "w" reescribe el archivo completo, de modo que las altas, bajas y
    modificaciones quedan reflejadas exactamente como estan en memoria.

    Parametros:
        inventario (list): lista de diccionarios con los productos.
        ruta       (str) : archivo destino.
    Retorna:
        bool: True si la informacion se grabo correctamente.
    """
    grabado = False
    try:
        os.makedirs(CARPETA_DATOS, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as archivo:
            for producto in inventario:
                archivo.write(producto_a_linea(producto))   # Metodo write()
    except PermissionError as error:
        print("  [!] No se pudo grabar el inventario (permisos):", error)
        registrar_error("guardar_inventario", str(error))
    except OSError as error:
        print("  [!] Error de escritura en disco:", error)
        registrar_error("guardar_inventario", str(error))
    else:
        grabado = True
        print("  [OK] Inventario grabado en '{0}' ({1} registro/s).".format(ruta, len(inventario)))
    finally:
        print("  [i] Operacion de guardado finalizada.")
    return grabado


def venta_a_linea(venta):
    """Convierte una venta (diccionario anidado) en una linea de texto.

    Formato: boleta;fecha;cliente;items;subtotal;igv;total
    donde items = id:cantidad:precio:descuento|id:cantidad:precio:descuento

    Parametros:
        venta (dict): venta construida por construir_venta().
    Retorna:
        str: linea lista para grabarse en ventas.txt
    """
    detalle = []
    for item in venta["items"]:
        campos_item = [
            item["id"],
            str(item["cantidad"]),
            "{0:.2f}".format(item["precio_unitario"]),
            "{0:.1f}".format(item["descuento"]),
        ]
        detalle.append(SEPARADOR_SUBCAMPO.join(campos_item))
    return "{0};{1};{2};{3};{4:.2f};{5:.2f};{6:.2f}\n".format(
        venta["boleta"], venta["fecha"], venta["cliente"],
        SEPARADOR_ITEM.join(detalle),
        venta["subtotal"], venta["igv"], venta["total"])


def linea_a_venta(linea):
    """Convierte una linea de ventas.txt en un diccionario anidado de venta.

    Parametros:
        linea (str): registro leido del historial.
    Retorna:
        dict: venta con su lista interna de items.
    Lanza:
        ValueError: si el registro esta incompleto o mal formado.
    """
    campos = linea.strip().split(SEPARADOR_CAMPO)
    if len(campos) != 7:
        raise ValueError("El registro de venta no tiene los 7 campos requeridos")

    items = []
    for bloque in campos[3].split(SEPARADOR_ITEM):
        datos = bloque.split(SEPARADOR_SUBCAMPO)
        if len(datos) != 4:
            raise ValueError("Item de venta mal formado")
        items.append({
            "id": datos[0],
            "cantidad": int(datos[1]),
            "precio_unitario": float(datos[2]),
            "descuento": float(datos[3]),
        })

    return {
        "boleta": campos[0],
        "fecha": campos[1],
        "cliente": campos[2],
        "items": items,
        "subtotal": float(campos[4]),
        "igv": float(campos[5]),
        "total": float(campos[6]),
    }


def cargar_ventas(ruta=ARCHIVO_VENTAS):
    """Carga el historial de ventas desde el archivo de texto (modo "r").

    Parametros:
        ruta (str): ubicacion del archivo de ventas.
    Retorna:
        list: lista de diccionarios con las ventas registradas.
    """
    ventas = []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()        # Metodo readlines()
    except FileNotFoundError:
        print("  [!] Aun no existe historial de ventas. Se creara al vender.")
        registrar_error("cargar_ventas", "FileNotFoundError: " + ruta)
    except OSError as error:
        print("  [!] No se pudo leer el historial de ventas:", error)
        registrar_error("cargar_ventas", str(error))
    else:
        for numero, linea in enumerate(lineas, start=1):
            if not linea.strip():
                continue
            try:
                ventas.append(linea_a_venta(linea))
            except ValueError as error:
                registrar_error("cargar_ventas", "Linea {0}: {1}".format(numero, error))
                continue
        print("  [OK] Historial cargado: {0} venta(s).".format(len(ventas)))
    finally:
        print("  [i] Proceso de lectura del historial finalizado.")
    return ventas


def registrar_venta_en_archivo(venta, ruta=ARCHIVO_VENTAS):
    """Agrega UNA venta al final del historial (modo "a" - append).

    A diferencia del inventario, el historial de ventas nunca se reescribe:
    cada transaccion se agrega al final para conservar la trazabilidad.

    Parametros:
        venta (dict): venta a registrar.
        ruta  (str) : archivo destino.
    Retorna:
        bool: True si la venta quedo grabada en disco.
    """
    grabada = False
    try:
        os.makedirs(CARPETA_DATOS, exist_ok=True)
        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(venta_a_linea(venta))     # write() en modo append
    except PermissionError as error:
        print("  [!] No se pudo registrar la venta (permisos):", error)
        registrar_error("registrar_venta_en_archivo", str(error))
    except OSError as error:
        print("  [!] Error al grabar la venta:", error)
        registrar_error("registrar_venta_en_archivo", str(error))
    else:
        grabada = True
    finally:
        print("  [i] Operacion de registro de venta finalizada.")
    return grabada


# =============================================================================
# CAPA 3: VALIDACION Y ENTRADA SEGURA DE DATOS
# -----------------------------------------------------------------------------
# Ninguna funcion de este bloque permite que una entrada incorrecta del usuario
# cierre inesperadamente el programa. Cada lectura se protege con la estructura
# completa try-except-else-finally y con un bucle while que insiste hasta
# obtener un dato valido (o hasta que el usuario cancele con la palabra "X").
# =============================================================================

def leer_cadena(mensaje, obligatorio=True, maximo=40, cancelable=True):
    """Lee texto desde el teclado validando longitud y obligatoriedad.

    Parametros:
        mensaje    (str) : indicacion mostrada al usuario.
        obligatorio(bool): si True, no se acepta una cadena vacia.
        maximo     (int) : cantidad maxima de caracteres permitidos.
        cancelable (bool): si True, la letra X cancela la operacion.
    Retorna:
        str : texto validado, o None si el usuario cancela la operacion.
    """
    while True:
        try:
            dato = input(mensaje).strip()
        except (EOFError, KeyboardInterrupt):
            # Ctrl+C / Ctrl+Z no deben provocar un cierre abrupto con traceback.
            print("\n  [i] Entrada interrumpida por el usuario.")
            return None
        except ValueError as error:
            registrar_error("leer_cadena", str(error))
            continue

        if cancelable and dato.upper() == "X":
            return None
        if not dato and obligatorio:
            print("  [!] El dato es obligatorio. Intente nuevamente.")
            continue
        if len(dato) > maximo:
            print("  [!] Maximo {0} caracteres. Intente nuevamente.".format(maximo))
            continue
        return dato


def leer_entero(mensaje, minimo=None, maximo=None, cancelable=True):
    """Lee un numero entero validando tipo de dato y rango permitido.

    Evita el error tipico de convertir texto no numerico con int(), capturando
    la excepcion ValueError y solicitando nuevamente el dato.

    Parametros:
        mensaje   (str): indicacion mostrada al usuario.
        minimo    (int): valor minimo aceptado (None = sin limite inferior).
        maximo    (int): valor maximo aceptado (None = sin limite superior).
        cancelable(bool): si True, la letra X cancela la operacion.
    Retorna:
        int : numero entero validado, o None si el usuario cancela.
    """
    while True:
        entrada = ""
        try:
            entrada = input(mensaje).strip()
            if cancelable and entrada.upper() == "X":
                return None
            numero = int(entrada)               # Puede lanzar ValueError
        except ValueError:
            print("  [!] Dato invalido: '{0}' no es un numero entero.".format(entrada))
            registrar_error("leer_entero", "ValueError con la entrada: " + entrada)
            continue
        except (EOFError, KeyboardInterrupt):
            print("\n  [i] Entrada interrumpida por el usuario.")
            return None
        else:
            # El bloque else solo se ejecuta si NO hubo excepcion.
            if minimo is not None and numero < minimo:
                print("  [!] El valor minimo permitido es {0}.".format(minimo))
                continue
            if maximo is not None and numero > maximo:
                print("  [!] El valor maximo permitido es {0}.".format(maximo))
                continue
            return numero


def leer_decimal(mensaje, minimo=0.0, maximo=None, cancelable=True):
    """Lee un numero decimal (float) validando tipo de dato y rango.

    Acepta coma o punto como separador decimal, error muy frecuente del
    personal administrativo que digita precios.

    Parametros:
        mensaje   (str)  : indicacion mostrada al usuario.
        minimo    (float): valor minimo aceptado.
        maximo    (float): valor maximo aceptado (None = sin limite).
        cancelable(bool) : si True, la letra X cancela la operacion.
    Retorna:
        float : numero validado, o None si el usuario cancela.
    """
    while True:
        entrada = ""
        try:
            entrada = input(mensaje).strip().replace(",", ".")
            if cancelable and entrada.upper() == "X":
                return None
            numero = float(entrada)             # Puede lanzar ValueError
        except ValueError:
            print("  [!] Dato invalido: ingrese un monto numerico (ej. 59.90).")
            registrar_error("leer_decimal", "ValueError con la entrada: " + entrada)
            continue
        except (EOFError, KeyboardInterrupt):
            print("\n  [i] Entrada interrumpida por el usuario.")
            return None
        else:
            if minimo is not None and numero < minimo:
                print("  [!] El monto no puede ser menor que {0:.2f}.".format(minimo))
                continue
            if maximo is not None and numero > maximo:
                print("  [!] El monto no puede superar {0:.2f}.".format(maximo))
                continue
            return round(numero, 2)


def leer_opcion(mensaje, opciones_validas):
    """Lee una opcion del menu y verifica que pertenezca a las permitidas.

    Parametros:
        mensaje         (str) : indicacion mostrada al usuario.
        opciones_validas(list): lista de cadenas con las opciones aceptadas.
    Retorna:
        str : opcion valida elegida por el usuario ("0" si se interrumpe).
    """
    while True:
        try:
            opcion = input(mensaje).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  [i] Sesion interrumpida. Se cerrara el sistema con seguridad.")
            return "0"

        if opcion in opciones_validas:
            return opcion
        print("  [!] Opcion '{0}' no valida. Elija una opcion del menu.".format(opcion))


def confirmar(mensaje):
    """Solicita una confirmacion S/N al usuario.

    Parametros:
        mensaje (str): pregunta mostrada al usuario.
    Retorna:
        bool: True si el usuario responde S, False en cualquier otro caso.
    """
    respuesta = leer_cadena(mensaje + " (S/N): ", obligatorio=True, maximo=3,
                            cancelable=False)
    return respuesta is not None and respuesta.upper() in ("S", "SI")


# =============================================================================
# CAPA 4: LOGICA DE NEGOCIO
# -----------------------------------------------------------------------------
# Reglas propias del negocio (busquedas, altas, calculos, reportes).
# IMPORTANTE: ninguna funcion de esta capa usa print() ni input(); todas
# reciben parametros y devuelven valores de retorno, por lo que son
# reutilizables y verificables de forma independiente a la consola.
# =============================================================================

def buscar_producto_por_id(inventario, id_producto):
    """Busca un producto por su identificador unico.

    Parametros:
        inventario  (list): lista de diccionarios con los productos.
        id_producto (str) : codigo a buscar (no distingue mayusculas).
    Retorna:
        dict : el producto encontrado, o None si no existe.
    """
    if id_producto is None:
        return None
    clave = id_producto.strip().upper()
    for producto in inventario:
        if producto["id"] == clave:
            return producto
    return None


def existe_id(inventario, id_producto):
    """Indica si un ID ya esta registrado (control de duplicados).

    Parametros:
        inventario  (list): lista de productos.
        id_producto (str) : codigo a verificar.
    Retorna:
        bool: True si el ID ya existe en el inventario.
    """
    return buscar_producto_por_id(inventario, id_producto) is not None


def buscar_productos_por_texto(inventario, texto):
    """Busca productos cuyo nombre o categoria contengan el texto indicado.

    Parametros:
        inventario (list): lista de productos.
        texto      (str) : palabra o fragmento a buscar.
    Retorna:
        list: productos coincidentes (lista vacia si no hay coincidencias).
    """
    patron = texto.strip().lower()
    coincidencias = []
    for producto in inventario:
        if patron in producto["nombre"].lower() or patron in producto["categoria"].lower():
            coincidencias.append(producto)
    return coincidencias


def generar_id_producto(inventario):
    """Genera automaticamente el siguiente ID correlativo (P001, P002, ...).

    Parametros:
        inventario (list): lista de productos existentes.
    Retorna:
        str: nuevo identificador unico sugerido.
    """
    mayor = 0
    for producto in inventario:
        try:
            numero = int(producto["id"][1:])
        except ValueError:
            continue                    # IDs manuales no correlativos se ignoran
        if numero > mayor:
            mayor = numero
    return "P{0:03d}".format(mayor + 1)


def crear_producto(id_producto, nombre, categoria, precio, stock):
    """Construye y valida el diccionario de un producto.

    Parametros:
        id_producto (str)  : codigo unico.
        nombre      (str)  : descripcion comercial.
        categoria   (str)  : familia a la que pertenece.
        precio      (float): precio unitario de venta.
        stock       (int)  : unidades disponibles.
    Retorna:
        dict: producto listo para incorporarse al inventario.
    Lanza:
        ValueError: si el precio o el stock son negativos, o falta el nombre.
    """
    if not nombre:
        raise ValueError("El nombre del producto es obligatorio")
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if stock < 0:
        raise ValueError("El stock no puede ser negativo")
    return {
        "id": id_producto.strip().upper(),
        "nombre": nombre.strip(),
        "categoria": categoria.strip(),
        "precio": round(float(precio), 2),
        "stock": int(stock),
    }


def agregar_producto(inventario, producto):
    """Da de alta un producto en el inventario controlando IDs duplicados.

    Parametros:
        inventario (list): lista de productos (se modifica en memoria).
        producto   (dict): producto validado por crear_producto().
    Retorna:
        bool: True si el alta fue exitosa.
    Lanza:
        ValueError: si el ID ya se encuentra registrado.
    """
    if existe_id(inventario, producto["id"]):
        raise ValueError("El ID {0} ya esta registrado".format(producto["id"]))
    inventario.append(producto)
    return True


def actualizar_precio(inventario, id_producto, nuevo_precio):
    """Modifica el precio unitario de un producto existente.

    Parametros:
        inventario   (list) : lista de productos.
        id_producto  (str)  : codigo del producto a modificar.
        nuevo_precio (float): nuevo precio de venta.
    Retorna:
        dict: el producto actualizado.
    Lanza:
        KeyError  : si el producto no existe.
        ValueError: si el precio es negativo.
    """
    producto = buscar_producto_por_id(inventario, id_producto)
    if producto is None:
        raise KeyError("Producto no encontrado: " + str(id_producto))
    if nuevo_precio < 0:
        raise ValueError("El precio no puede ser negativo")
    producto["precio"] = round(float(nuevo_precio), 2)
    return producto


def actualizar_stock(inventario, id_producto, movimiento):
    """Aplica un movimiento de stock (positivo ingreso, negativo salida).

    Parametros:
        inventario  (list): lista de productos.
        id_producto (str) : codigo del producto.
        movimiento  (int) : unidades a sumar (+) o restar (-).
    Retorna:
        int: stock resultante despues del movimiento.
    Lanza:
        KeyError  : si el producto no existe.
        ValueError: si el movimiento dejaria el stock en negativo.
    """
    producto = buscar_producto_por_id(inventario, id_producto)
    if producto is None:
        raise KeyError("Producto no encontrado: " + str(id_producto))
    resultante = producto["stock"] + int(movimiento)
    if resultante < 0:
        raise ValueError("Stock insuficiente: disponible {0}, solicitado {1}".format(
            producto["stock"], abs(movimiento)))
    producto["stock"] = resultante
    return resultante


def eliminar_producto(inventario, id_producto):
    """Da de baja un producto del catalogo.

    Parametros:
        inventario  (list): lista de productos.
        id_producto (str) : codigo del producto a eliminar.
    Retorna:
        dict: el producto retirado del inventario.
    Lanza:
        KeyError: si el producto no existe.
    """
    producto = buscar_producto_por_id(inventario, id_producto)
    if producto is None:
        raise KeyError("Producto no encontrado: " + str(id_producto))
    inventario.remove(producto)
    return producto


def calcular_descuento(cantidad):
    """Determina el porcentaje de descuento por volumen de compra.

    Escala comercial vigente:
        12 unidades o mas ... 12 %
         6 a 11 unidades .... 8 %
         3 a  5 unidades .... 5 %
        menos de 3 ......... sin descuento

    Parametros:
        cantidad (int): unidades solicitadas del producto.
    Retorna:
        float: porcentaje de descuento aplicable.
    """
    for minimo, porcentaje in ESCALA_DESCUENTOS:
        if cantidad >= minimo:
            return porcentaje
    return 0.0


def calcular_importe_item(cantidad, precio_unitario, descuento):
    """Calcula el importe neto de una linea de venta.

    Parametros:
        cantidad        (int)  : unidades vendidas.
        precio_unitario (float): precio de lista.
        descuento       (float): porcentaje de descuento aplicado.
    Retorna:
        float: importe con descuento aplicado, redondeado a 2 decimales.
    """
    bruto = cantidad * precio_unitario
    return round(bruto - (bruto * descuento / 100.0), 2)


def crear_item_venta(producto, cantidad):
    """Construye la linea de detalle de una venta a partir de un producto.

    Parametros:
        producto (dict): producto del inventario.
        cantidad (int) : unidades solicitadas.
    Retorna:
        dict: item con cantidad, precio, descuento e importe.
    Lanza:
        ValueError: si la cantidad no es positiva o supera el stock.
    """
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero")
    if cantidad > producto["stock"]:
        raise ValueError("Stock insuficiente: solo quedan {0} unidad(es)".format(
            producto["stock"]))
    descuento = calcular_descuento(cantidad)
    return {
        "id": producto["id"],
        "nombre": producto["nombre"],
        "cantidad": cantidad,
        "precio_unitario": producto["precio"],
        "descuento": descuento,
        "importe": calcular_importe_item(cantidad, producto["precio"], descuento),
    }


def generar_numero_boleta(ventas):
    """Genera el numero correlativo de la siguiente boleta (B0001, B0002, ...).

    Parametros:
        ventas (list): historial de ventas registradas.
    Retorna:
        str: numero de boleta correlativo.
    """
    return "B{0:04d}".format(len(ventas) + 1)


def construir_venta(numero_boleta, cliente, items):
    """Arma el comprobante de venta con sus totales e impuestos.

    Estructura resultante (diccionario anidado):
        {boleta, fecha, cliente, items:[{...}, {...}], subtotal, igv, total}

    Parametros:
        numero_boleta (str) : correlativo del comprobante.
        cliente       (str) : nombre del cliente.
        items         (list): lineas de detalle de la venta.
    Retorna:
        dict: comprobante de venta completo.
    Lanza:
        ValueError: si la venta no contiene items.
    """
    if not items:
        raise ValueError("La venta debe contener al menos un producto")
    subtotal = round(sum(item["importe"] for item in items), 2)
    igv = round(subtotal * IGV, 2)
    return {
        "boleta": numero_boleta,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "cliente": cliente if cliente else "CLIENTE VARIOS",
        "items": items,
        "subtotal": subtotal,
        "igv": igv,
        "total": round(subtotal + igv, 2),
    }


def descontar_stock_de_venta(inventario, items):
    """Descuenta del inventario las unidades vendidas de cada item.

    Parametros:
        inventario (list): lista de productos.
        items      (list): lineas de detalle de la venta.
    Retorna:
        int: cantidad de productos cuyo stock fue actualizado.
    """
    actualizados = 0
    for item in items:
        actualizar_stock(inventario, item["id"], -item["cantidad"])
        actualizados += 1
    return actualizados


def valorizar_inventario(inventario):
    """Calcula el valor total del inventario a precio de venta.

    Parametros:
        inventario (list): lista de productos.
    Retorna:
        float: sumatoria de precio * stock de todos los productos.
    """
    return round(sum(p["precio"] * p["stock"] for p in inventario), 2)


def productos_stock_critico(inventario, minimo=STOCK_MINIMO):
    """Devuelve los productos que requieren reposicion urgente.

    Parametros:
        inventario (list): lista de productos.
        minimo     (int) : umbral de stock critico.
    Retorna:
        list: productos con stock menor o igual al umbral.
    """
    return [p for p in inventario if p["stock"] <= minimo]


def resumen_ventas(ventas, fecha=None):
    """Consolida los indicadores del historial de ventas.

    Parametros:
        ventas (list): historial de ventas.
        fecha  (str) : dia a filtrar con formato dd/mm/aaaa (None = todo).
    Retorna:
        dict: {cantidad, subtotal, igv, total, ticket_promedio, unidades}
    """
    seleccion = ventas
    if fecha is not None:
        seleccion = [v for v in ventas if v["fecha"].startswith(fecha)]

    total = round(sum(v["total"] for v in seleccion), 2)
    unidades = sum(item["cantidad"] for v in seleccion for item in v["items"])
    cantidad = len(seleccion)
    return {
        "cantidad": cantidad,
        "subtotal": round(sum(v["subtotal"] for v in seleccion), 2),
        "igv": round(sum(v["igv"] for v in seleccion), 2),
        "total": total,
        "unidades": unidades,
        "ticket_promedio": round(total / cantidad, 2) if cantidad else 0.0,
    }


def ranking_productos(ventas, top=5):
    """Determina los productos mas vendidos del historial.

    Parametros:
        ventas (list): historial de ventas.
        top    (int) : cantidad de posiciones a devolver.
    Retorna:
        list: tuplas (id, unidades vendidas) ordenadas de mayor a menor.
    """
    acumulado = {}                          # Diccionario id -> unidades
    for venta in ventas:
        for item in venta["items"]:
            acumulado[item["id"]] = acumulado.get(item["id"], 0) + item["cantidad"]
    ordenado = sorted(acumulado.items(), key=lambda par: par[1], reverse=True)
    return ordenado[:top]


# =============================================================================
# CAPA 5: INTERFAZ DE CONSOLA
# -----------------------------------------------------------------------------
# Unico lugar del programa donde se usan print() e input() para dialogar con el
# usuario. Se apoya en la CAPA 3 para validar y en la CAPA 4 para calcular.
# =============================================================================

def limpiar_pantalla():
    """Limpia la consola segun el sistema operativo (Windows / Linux / Mac)."""
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except OSError:
        print("\n" * 3)


def mostrar_encabezado(titulo):
    """Imprime el encabezado estandar de cada modulo del sistema.

    Parametros:
        titulo (str): nombre de la operacion en curso.
    """
    print("=" * ANCHO)
    print("  {0}".format(NOMBRE_EMPRESA).ljust(ANCHO - 24) +
          datetime.now().strftime("%d/%m/%Y %H:%M"))
    print("  {0}".format(titulo.upper()))
    print("=" * ANCHO)


def mostrar_menu_principal():
    """Muestra el menu principal con todas las operaciones disponibles."""
    print("=" * ANCHO)
    print("{0:^{1}}".format("SISTEMA DE GESTION DE INVENTARIO Y VENTAS", ANCHO))
    print("{0:^{1}}".format(NOMBRE_EMPRESA + " - " + RUBRO_EMPRESA, ANCHO))
    print("=" * ANCHO)
    print("   GESTION DE INVENTARIO                 VENTAS Y REPORTES")
    print("   ---------------------                 -----------------")
    print("   [1] Listar inventario                 [5] Registrar venta")
    print("   [2] Registrar nuevo producto          [6] Historial de ventas")
    print("   [3] Buscar producto                   [7] Reporte de inventario")
    print("   [4] Actualizar producto               [8] Reporte de ventas")
    print("                                         [9] Guardar cambios")
    print("   [0] Salir del sistema")
    print("=" * ANCHO)


def mostrar_tabla_productos(productos):
    """Presenta una lista de productos en formato de tabla alineada.

    Parametros:
        productos (list): productos a mostrar.
    Retorna:
        int: cantidad de productos mostrados.
    """
    if not productos:
        print("  [i] No hay productos que mostrar.")
        return 0

    print("-" * ANCHO)
    print(" {0:<6} {1:<26} {2:<14} {3:>10} {4:>7} {5:>9}".format(
        "ID", "PRODUCTO", "CATEGORIA", "PRECIO S/", "STOCK", "ESTADO"))
    print("-" * ANCHO)
    for producto in productos:
        if producto["stock"] == 0:
            estado = "AGOTADO"
        elif producto["stock"] <= STOCK_MINIMO:
            estado = "CRITICO"
        else:
            estado = "OK"
        print(" {0:<6} {1:<26} {2:<14} {3:>10.2f} {4:>7} {5:>9}".format(
            producto["id"], producto["nombre"][:26], producto["categoria"][:14],
            producto["precio"], producto["stock"], estado))
    print("-" * ANCHO)
    print(" Total de productos listados: {0}".format(len(productos)))
    return len(productos)


def mostrar_comprobante(venta):
    """Imprime en pantalla el comprobante (boleta) de una venta.

    Parametros:
        venta (dict): comprobante generado por construir_venta().
    """
    print()
    print("+" + "-" * (ANCHO - 2) + "+")
    print("|{0:^{1}}|".format(NOMBRE_EMPRESA, ANCHO - 2))
    print("|{0:^{1}}|".format("BOLETA DE VENTA ELECTRONICA  " + venta["boleta"], ANCHO - 2))
    print("+" + "-" * (ANCHO - 2) + "+")
    print(" Fecha  : {0}".format(venta["fecha"]))
    print(" Cliente: {0}".format(venta["cliente"]))
    print("-" * ANCHO)
    print(" {0:<6} {1:<24} {2:>5} {3:>10} {4:>7} {5:>11}".format(
        "ID", "DESCRIPCION", "CANT", "P.UNIT", "DSCTO%", "IMPORTE"))
    print("-" * ANCHO)
    for item in venta["items"]:
        print(" {0:<6} {1:<24} {2:>5} {3:>10.2f} {4:>7.1f} {5:>11.2f}".format(
            item["id"], item.get("nombre", "")[:24], item["cantidad"],
            item["precio_unitario"], item["descuento"], item["importe"]))
    print("-" * ANCHO)
    print("{0:>66} {1:>11.2f}".format("SUBTOTAL S/", venta["subtotal"]))
    print("{0:>66} {1:>11.2f}".format("IGV (18%) S/", venta["igv"]))
    print("{0:>66} {1:>11.2f}".format("TOTAL S/", venta["total"]))
    print("=" * ANCHO)


def pausar():
    """Detiene la ejecucion hasta que el usuario presione ENTER."""
    try:
        input("\n  Presione ENTER para volver al menu principal...")
    except (EOFError, KeyboardInterrupt):
        print()


# -----------------------------------------------------------------------------
# OPERACIONES DEL MENU (una funcion por cada opcion: separacion clara)
# -----------------------------------------------------------------------------

def opcion_listar_inventario(inventario):
    """Opcion 1: muestra todo el catalogo de productos.

    Parametros:
        inventario (list): lista de productos en memoria.
    """
    mostrar_encabezado("Listado general del inventario")
    mostrar_tabla_productos(inventario)
    if inventario:
        print(" Valorizado total del inventario: S/ {0:,.2f}".format(
            valorizar_inventario(inventario)))


def opcion_registrar_producto(inventario):
    """Opcion 2: da de alta un producto nuevo en el inventario.

    Valida el ID duplicado, el precio y el stock antes de aceptar el registro.

    Parametros:
        inventario (list): lista de productos (se modifica en memoria).
    Retorna:
        bool: True si el producto fue registrado.
    """
    mostrar_encabezado("Registro de nuevo producto")
    print("  (Escriba X en cualquier momento para cancelar la operacion)\n")

    sugerido = generar_id_producto(inventario)
    id_producto = leer_cadena("  ID del producto [ENTER = {0}]: ".format(sugerido),
                              obligatorio=False, maximo=6)
    if id_producto is None:
        print("\n  [i] Operacion cancelada por el usuario.")
        return False
    if not id_producto:
        id_producto = sugerido

    if existe_id(inventario, id_producto):
        print("  [!] El ID '{0}' ya existe. No se permiten duplicados.".format(
            id_producto.upper()))
        return False

    nombre = leer_cadena("  Nombre del producto            : ", maximo=26)
    if nombre is None:
        print("\n  [i] Operacion cancelada por el usuario.")
        return False

    print("  Categorias disponibles: " + ", ".join(
        "{0}={1}".format(i + 1, c) for i, c in enumerate(CATEGORIAS)))
    indice = leer_entero("  Categoria (1-{0})                : ".format(len(CATEGORIAS)),
                         minimo=1, maximo=len(CATEGORIAS))
    if indice is None:
        print("\n  [i] Operacion cancelada por el usuario.")
        return False
    categoria = CATEGORIAS[indice - 1]

    precio = leer_decimal("  Precio unitario de venta S/    : ", minimo=0.10, maximo=99999.0)
    if precio is None:
        print("\n  [i] Operacion cancelada por el usuario.")
        return False

    stock = leer_entero("  Stock inicial (unidades)       : ", minimo=0, maximo=99999)
    if stock is None:
        print("\n  [i] Operacion cancelada por el usuario.")
        return False

    registrado = False
    try:
        producto = crear_producto(id_producto, nombre, categoria, precio, stock)
        agregar_producto(inventario, producto)
    except ValueError as error:
        print("\n  [!] No se pudo registrar el producto: {0}".format(error))
        registrar_error("opcion_registrar_producto", str(error))
    else:
        registrado = True
        print("\n  [OK] Producto '{0}' registrado con el codigo {1}.".format(
            producto["nombre"], producto["id"]))
        guardar_inventario(inventario)      # Persistencia inmediata
    finally:
        print("  [i] Fin del proceso de alta de producto.")
    return registrado


def opcion_buscar_producto(inventario):
    """Opcion 3: busca productos por codigo o por texto libre.

    Parametros:
        inventario (list): lista de productos.
    """
    mostrar_encabezado("Busqueda de productos")
    if not inventario:
        print("  [i] El inventario esta vacio. Registre productos primero.")
        return

    print("  [1] Buscar por ID exacto")
    print("  [2] Buscar por nombre o categoria")
    tipo = leer_opcion("\n  Seleccione el tipo de busqueda: ", ["1", "2"])

    if tipo == "1":
        id_producto = leer_cadena("  Ingrese el ID a consultar: ", maximo=6)
        if id_producto is None:
            return
        producto = buscar_producto_por_id(inventario, id_producto)
        if producto is None:
            print("\n  [!] No existe un producto con el codigo '{0}'.".format(
                id_producto.upper()))
        else:
            print()
            mostrar_tabla_productos([producto])
            print(" Valorizado de este producto: S/ {0:,.2f}".format(
                producto["precio"] * producto["stock"]))
    else:
        texto = leer_cadena("  Ingrese el texto a buscar: ", maximo=26)
        if texto is None:
            return
        coincidencias = buscar_productos_por_texto(inventario, texto)
        print()
        if not coincidencias:
            print("  [!] Sin coincidencias para '{0}'.".format(texto))
        else:
            mostrar_tabla_productos(coincidencias)


def opcion_actualizar_producto(inventario):
    """Opcion 4: modifica precio, stock o da de baja un producto.

    Parametros:
        inventario (list): lista de productos.
    Retorna:
        bool: True si se realizo alguna modificacion.
    """
    mostrar_encabezado("Actualizacion de productos")
    if not inventario:
        print("  [i] El inventario esta vacio. Registre productos primero.")
        return False

    id_producto = leer_cadena("  ID del producto a actualizar (X = cancelar): ", maximo=6)
    if id_producto is None:
        print("\n  [i] Operacion cancelada por el usuario.")
        return False

    producto = buscar_producto_por_id(inventario, id_producto)
    if producto is None:
        print("\n  [!] No existe un producto con el codigo '{0}'.".format(
            id_producto.upper()))
        return False

    print()
    mostrar_tabla_productos([producto])
    print("\n  [1] Modificar precio de venta")
    print("  [2] Registrar ingreso de mercaderia (sumar stock)")
    print("  [3] Registrar merma o ajuste (restar stock)")
    print("  [4] Dar de baja el producto")
    accion = leer_opcion("\n  Seleccione la accion: ", ["1", "2", "3", "4"])

    modificado = False
    try:
        if accion == "1":
            nuevo = leer_decimal("  Nuevo precio S/ : ", minimo=0.10, maximo=99999.0)
            if nuevo is None:
                raise ValueError("Operacion cancelada por el usuario")
            anterior = producto["precio"]
            actualizar_precio(inventario, producto["id"], nuevo)
            print("\n  [OK] Precio actualizado: S/ {0:.2f} -> S/ {1:.2f}".format(
                anterior, producto["precio"]))
        elif accion == "2":
            unidades = leer_entero("  Unidades que ingresan: ", minimo=1, maximo=9999)
            if unidades is None:
                raise ValueError("Operacion cancelada por el usuario")
            resultante = actualizar_stock(inventario, producto["id"], unidades)
            print("\n  [OK] Stock actualizado. Nuevo stock: {0} unidad(es).".format(resultante))
        elif accion == "3":
            unidades = leer_entero("  Unidades que salen: ", minimo=1, maximo=9999)
            if unidades is None:
                raise ValueError("Operacion cancelada por el usuario")
            resultante = actualizar_stock(inventario, producto["id"], -unidades)
            print("\n  [OK] Stock actualizado. Nuevo stock: {0} unidad(es).".format(resultante))
        else:
            if not confirmar("\n  Confirma dar de baja '{0}'?".format(producto["nombre"])):
                raise ValueError("Baja no confirmada por el usuario")
            eliminado = eliminar_producto(inventario, producto["id"])
            print("\n  [OK] Producto '{0}' dado de baja del catalogo.".format(
                eliminado["nombre"]))
    except ValueError as error:
        print("\n  [!] Operacion no realizada: {0}".format(error))
        registrar_error("opcion_actualizar_producto", str(error))
    except KeyError as error:
        print("\n  [!] Producto no encontrado: {0}".format(error))
        registrar_error("opcion_actualizar_producto", str(error))
    else:
        modificado = True
        guardar_inventario(inventario)      # Persistencia inmediata
    finally:
        print("  [i] Fin del proceso de actualizacion.")
    return modificado


def opcion_registrar_venta(inventario, ventas):
    """Opcion 5: registra una transaccion de venta con varios productos.

    Flujo: se agregan items en un bucle while (break para terminar, continue
    ante errores), se calculan descuentos e IGV, se descuenta el stock y se
    graba la venta en el historial (modo "a") y el inventario (modo "w").

    Parametros:
        inventario (list): lista de productos.
        ventas     (list): historial de ventas en memoria.
    Retorna:
        bool: True si la venta se registro correctamente.
    """
    mostrar_encabezado("Registro de venta")
    disponibles = [p for p in inventario if p["stock"] > 0]
    if not disponibles:
        print("  [!] No hay productos con stock disponible para vender.")
        return False

    mostrar_tabla_productos(disponibles)

    cliente = leer_cadena("\n  Nombre del cliente [ENTER = CLIENTE VARIOS]: ",
                          obligatorio=False, maximo=30)
    if cliente is None:
        print("\n  [i] Venta cancelada por el usuario.")
        return False

    items = []
    print("\n  Agregue los productos de la venta (escriba F para finalizar).")
    while True:
        id_producto = leer_cadena("\n  ID del producto (F = finalizar): ",
                                  maximo=6, cancelable=False)
        if id_producto is None or id_producto.upper() == "F":
            break                           # Termina la carga de items

        producto = buscar_producto_por_id(inventario, id_producto)
        if producto is None:
            print("  [!] El producto '{0}' no existe en el catalogo.".format(
                id_producto.upper()))
            continue                        # Vuelve a pedir el ID
        if producto["stock"] <= 0:
            print("  [!] '{0}' se encuentra AGOTADO.".format(producto["nombre"]))
            continue

        cantidad = leer_entero("  Cantidad (stock disponible {0}): ".format(
            producto["stock"]), minimo=1, maximo=99999)
        if cantidad is None:
            print("  [i] Item descartado.")
            continue

        try:
            item = crear_item_venta(producto, cantidad)
        except ValueError as error:
            print("  [!] {0}".format(error))
            registrar_error("opcion_registrar_venta", str(error))
            continue                        # El item no se agrega, la venta sigue
        else:
            items.append(item)
            print("  [OK] Agregado: {0} x {1} = S/ {2:.2f} (dscto {3:.1f}%)".format(
                cantidad, item["nombre"], item["importe"], item["descuento"]))

    if not items:
        print("\n  [i] La venta fue anulada: no se agregaron productos.")
        return False

    registrada = False
    try:
        venta = construir_venta(generar_numero_boleta(ventas), cliente, items)
        descontar_stock_de_venta(inventario, items)
    except ValueError as error:
        print("\n  [!] No se pudo procesar la venta: {0}".format(error))
        registrar_error("opcion_registrar_venta", str(error))
    except KeyError as error:
        print("\n  [!] Error de integridad del inventario: {0}".format(error))
        registrar_error("opcion_registrar_venta", str(error))
    else:
        ventas.append(venta)
        mostrar_comprobante(venta)
        registrar_venta_en_archivo(venta)   # Modo "a": agrega al historial
        guardar_inventario(inventario)      # Modo "w": stock actualizado
        registrada = True
    finally:
        print("  [i] Transaccion finalizada.")
    return registrada


def opcion_historial_ventas(ventas):
    """Opcion 6: lista las ventas registradas en el historial.

    Parametros:
        ventas (list): historial de ventas.
    """
    mostrar_encabezado("Historial de ventas")
    if not ventas:
        print("  [i] Aun no se han registrado ventas.")
        return

    print("-" * ANCHO)
    print(" {0:<8} {1:<20} {2:<24} {3:>6} {4:>12}".format(
        "BOLETA", "FECHA", "CLIENTE", "ITEMS", "TOTAL S/"))
    print("-" * ANCHO)
    for venta in ventas:
        print(" {0:<8} {1:<20} {2:<24} {3:>6} {4:>12.2f}".format(
            venta["boleta"], venta["fecha"], venta["cliente"][:24],
            len(venta["items"]), venta["total"]))
    print("-" * ANCHO)
    resumen = resumen_ventas(ventas)
    print(" Comprobantes: {0}   Unidades vendidas: {1}   Recaudado: S/ {2:,.2f}".format(
        resumen["cantidad"], resumen["unidades"], resumen["total"]))


def opcion_reporte_inventario(inventario):
    """Opcion 7: genera el reporte de situacion del inventario.

    Parametros:
        inventario (list): lista de productos.
    """
    mostrar_encabezado("Reporte de inventario")
    if not inventario:
        print("  [i] El inventario esta vacio.")
        return

    unidades = sum(p["stock"] for p in inventario)
    criticos = productos_stock_critico(inventario)
    agotados = [p for p in inventario if p["stock"] == 0]

    print(" Productos registrados .......: {0}".format(len(inventario)))
    print(" Unidades totales en stock ...: {0}".format(unidades))
    print(" Valorizado del inventario ...: S/ {0:,.2f}".format(
        valorizar_inventario(inventario)))
    print(" Productos en stock critico ..: {0} (umbral {1} unidades)".format(
        len(criticos), STOCK_MINIMO))
    print(" Productos agotados ..........: {0}".format(len(agotados)))

    print("\n RESUMEN POR CATEGORIA")
    print("-" * ANCHO)
    print(" {0:<16} {1:>10} {2:>12} {3:>16}".format(
        "CATEGORIA", "PRODUCTOS", "UNIDADES", "VALORIZADO S/"))
    print("-" * ANCHO)
    for categoria in CATEGORIAS:
        grupo = [p for p in inventario if p["categoria"] == categoria]
        if not grupo:
            continue
        print(" {0:<16} {1:>10} {2:>12} {3:>16,.2f}".format(
            categoria, len(grupo), sum(p["stock"] for p in grupo),
            valorizar_inventario(grupo)))
    print("-" * ANCHO)

    if criticos:
        print("\n ALERTA: PRODUCTOS QUE REQUIEREN REPOSICION")
        mostrar_tabla_productos(criticos)


def opcion_reporte_ventas(ventas):
    """Opcion 8: genera el reporte de rendimiento de ventas.

    Parametros:
        ventas (list): historial de ventas.
    """
    mostrar_encabezado("Reporte de ventas")
    if not ventas:
        print("  [i] Aun no se han registrado ventas.")
        return

    hoy = datetime.now().strftime("%d/%m/%Y")
    del_dia = resumen_ventas(ventas, hoy)
    historico = resumen_ventas(ventas)

    print(" VENTAS DEL DIA {0}".format(hoy))
    print("-" * ANCHO)
    print(" Comprobantes emitidos .......: {0}".format(del_dia["cantidad"]))
    print(" Unidades vendidas ...........: {0}".format(del_dia["unidades"]))
    print(" Venta neta (sin IGV) ........: S/ {0:,.2f}".format(del_dia["subtotal"]))
    print(" IGV del dia .................: S/ {0:,.2f}".format(del_dia["igv"]))
    print(" Total recaudado .............: S/ {0:,.2f}".format(del_dia["total"]))
    print(" Ticket promedio .............: S/ {0:,.2f}".format(del_dia["ticket_promedio"]))

    print("\n ACUMULADO HISTORICO")
    print("-" * ANCHO)
    print(" Comprobantes ................: {0}".format(historico["cantidad"]))
    print(" Total recaudado .............: S/ {0:,.2f}".format(historico["total"]))
    print(" Ticket promedio .............: S/ {0:,.2f}".format(historico["ticket_promedio"]))

    ranking = ranking_productos(ventas)
    if ranking:
        print("\n PRODUCTOS MAS VENDIDOS")
        print("-" * ANCHO)
        print(" {0:<8} {1:<30} {2:>12}".format("ID", "PRODUCTO", "UNIDADES"))
        print("-" * ANCHO)
        for posicion, (id_producto, unidades) in enumerate(ranking, start=1):
            nombre = "(producto retirado del catalogo)"
            for venta in ventas:
                for item in venta["items"]:
                    if item["id"] == id_producto and item.get("nombre"):
                        nombre = item["nombre"]
                        break
            print(" {0:<8} {1:<30} {2:>12}".format(id_producto, nombre[:30], unidades))
        print("-" * ANCHO)


def opcion_guardar_cambios(inventario):
    """Opcion 9: fuerza el guardado del inventario en el archivo de texto.

    Parametros:
        inventario (list): lista de productos.
    Retorna:
        bool: True si el guardado fue exitoso.
    """
    mostrar_encabezado("Guardado de informacion")
    resultado = guardar_inventario(inventario)
    if resultado:
        print("\n  [OK] La informacion quedara disponible en la proxima ejecucion.")
    else:
        print("\n  [!] Revise el archivo datos/errores.log para mayor detalle.")
    return resultado


# =============================================================================
# CONTROLADOR PRINCIPAL
# -----------------------------------------------------------------------------
# Bucle while que mantiene el menu activo e if-elif-else que deriva cada
# opcion hacia su funcion especializada. Es la unica funcion que coordina; no
# contiene reglas de negocio ni accesos directos a disco.
# =============================================================================

def cargar_datos_iniciales():
    """Carga inventario e historial desde los archivos al iniciar el sistema.

    Retorna:
        tuple: (inventario, ventas) como listas de diccionarios.
    """
    mostrar_encabezado("Inicializando el sistema")
    inicializar_almacenamiento()
    inventario = cargar_inventario()
    ventas = cargar_ventas()
    print("-" * ANCHO)
    return inventario, ventas


def main():
    """Punto de entrada del sistema: menu principal persistente.

    Estructura de control:
        while True ............ mantiene el menu activo hasta elegir salir.
        if - elif - else ...... deriva la opcion hacia su funcion modular.
        break ................. unica salida controlada del bucle.
    """
    inventario, ventas = cargar_datos_iniciales()
    pausar()

    while True:
        limpiar_pantalla()
        mostrar_menu_principal()
        opcion = leer_opcion("  Seleccione una opcion [0-9]: ", OPCIONES_MENU)
        print()

        if opcion == "1":
            opcion_listar_inventario(inventario)
        elif opcion == "2":
            opcion_registrar_producto(inventario)
        elif opcion == "3":
            opcion_buscar_producto(inventario)
        elif opcion == "4":
            opcion_actualizar_producto(inventario)
        elif opcion == "5":
            opcion_registrar_venta(inventario, ventas)
        elif opcion == "6":
            opcion_historial_ventas(ventas)
        elif opcion == "7":
            opcion_reporte_inventario(inventario)
        elif opcion == "8":
            opcion_reporte_ventas(ventas)
        elif opcion == "9":
            opcion_guardar_cambios(inventario)
        else:
            # Opcion "0": salida controlada con guardado de seguridad.
            mostrar_encabezado("Cierre del sistema")
            guardar_inventario(inventario)
            print("\n  Resumen de la sesion:")
            print("   - Productos en catalogo : {0}".format(len(inventario)))
            print("   - Ventas registradas    : {0}".format(len(ventas)))
            print("   - Valorizado final      : S/ {0:,.2f}".format(
                valorizar_inventario(inventario)))
            print("\n  Gracias por utilizar el sistema. Hasta pronto!")
            print("=" * ANCHO)
            break                           # Unica salida del bucle principal

        pausar()


# =============================================================================
# ARRANQUE DEL PROGRAMA
# -----------------------------------------------------------------------------
# La condicion __name__ == "__main__" permite que el archivo se ejecute como
# programa y, a la vez, que sus funciones puedan importarse desde otro modulo
# sin que el menu se dispare automaticamente.
# =============================================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  [i] Ejecucion interrumpida con Ctrl+C. Cierre seguro del sistema.")
    except Exception as error:              # Red de seguridad de ultimo nivel
        print("\n  [!] Error inesperado: {0}".format(error))
        registrar_error("main", "{0}: {1}".format(type(error).__name__, error))
        print("  [i] El detalle tecnico se registro en '{0}'.".format(ARCHIVO_LOG))
    finally:
        print("  [i] Proceso finalizado. Codigo de salida 0.")
        sys.exit(0)
