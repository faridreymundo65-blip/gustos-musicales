# CRUD de Alumnos con Python y MySQL

Guia paso a paso, en el mismo orden de las capturas de pantalla.

## 1. Crear la tabla Alumnos (`01_Tabla_Alumnos`)

Abre MySQL Workbench (o la consola de MySQL) y ejecuta el archivo `alumnos.sql`.
Crea la base `escuela` y la tabla `alumnos` con: id, matricula, nombre,
apellido, edad y carrera.

Desde la terminal tambien puedes hacerlo asi:

```powershell
mysql -u root -p < alumnos.sql
```

## 2. Abrir la terminal (`02_Comando`)

En Windows: tecla Windows -> escribe `cmd` o `PowerShell` -> Enter.

## 3. Crear las carpetas del proyecto (`03_Creo_carpetas`)

```powershell
mkdir C:\proyectos\crud_alumnos
cd C:\proyectos\crud_alumnos
python -m venv venv
```

`venv` es el entorno virtual: una copia aislada de Python solo para este
proyecto, para no ensuciar la instalacion global.

## 4. Activar el entorno virtual (`04_activar`)

```powershell
venv\Scripts\activate
```

Sabes que funciono porque al inicio de la linea aparece `(venv)`.

> Si PowerShell te dice "la ejecucion de scripts esta deshabilitada", corre una
> sola vez:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

## 5. Abrir Visual Studio Code (`05_Ir_visual_studio`)

```powershell
code .
```

Dentro de VS Code: `Ctrl + Shift + P` -> "Python: Select Interpreter" ->
elige el que dice `venv`.

## 6. Instalar el conector de MySQL (`06_Instala_mysql`)

Con el entorno activado `(venv)`:

```powershell
pip install mysql-connector-python
```

O bien: `pip install -r requirements.txt`

## 7. Probar la conexion desde PowerShell (`07_PowerShell`)

Edita `conexion.py` y pon tu contrasena real de MySQL en `CONFIG["password"]`.
Luego:

```powershell
python conexion.py
```

Debe imprimir: `Conexion exitosa a la base de datos 'escuela'`.

Si falla, revisa en este orden: que el servicio de MySQL este encendido, que la
contrasena sea la correcta y que la base `escuela` exista (paso 1).

## 8. Ejecutar el CRUD (`08_Crud_py`)

```powershell
python crud.py
```

Aparece el menu con las cuatro operaciones:

| Letra | Operacion | SQL      | Funcion en `crud.py` |
|-------|-----------|----------|----------------------|
| C     | Create    | `INSERT` | `crear()`            |
| R     | Read      | `SELECT` | `leer()`             |
| U     | Update    | `UPDATE` | `actualizar()`       |
| D     | Delete    | `DELETE` | `eliminar()`         |

## Archivos

- `alumnos.sql` — base de datos y tabla.
- `conexion.py` — datos de conexion a MySQL.
- `crud.py` — menu y las cuatro operaciones.
- `requirements.txt` — dependencias.

## Errores mas comunes

- `Access denied for user 'root'@'localhost'` — contrasena incorrecta en `conexion.py`.
- `Unknown database 'escuela'` — falta ejecutar `alumnos.sql`.
- `ModuleNotFoundError: No module named 'mysql'` — no activaste el `venv` (paso 4)
  o no instalaste el conector (paso 6).
- `Can't connect to MySQL server` — el servicio de MySQL esta apagado.
