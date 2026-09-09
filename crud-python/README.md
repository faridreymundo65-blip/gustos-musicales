# CRUD de Alumnos — Python + MySQL (Curso_Phyton / 00_BD_CRUD)

Guia paso a paso, en el mismo orden de las capturas del curso.

Estructura real del proyecto en tu PC:

```
D:\Curso_Phyton\00_BD_CRUD\
    Entornos\
        crudPy\          <- entorno virtual (Include, Lib, Scripts, pyvenv.cfg)
    crud.py              <- el programa
    CRUD_MySql.txt
```

Base de datos: **matricula** · Tabla: **alumno** · Servidor: localhost (phpMyAdmin muestra el puerto 3307)

---

## 1. Revisar la tabla en phpMyAdmin (`01_Tabla_Alumnos`)

Abre `http://localhost/phpmyadmin` → base de datos **matricula** → tabla **alumno**.

Columnas: `cod_alumno`, `pat_alu`, `mat_alu`, `nom_alu`, `edad_alu`,
`sexo_alu`, `direc_alu`, `dist_alu`, `correo_alu`.
El codigo es texto (ALU-001, ALU-002...), no un numero automatico.

El archivo `alumno.sql` de esta carpeta documenta esa estructura.

## 2. Abrir la consola (`02_Comando`)

```cmd
cd D:\Curso_Phyton\00_BD_CRUD\Entornos
python -m venv crudPy
```

`python -m venv crudPy` crea el entorno virtual llamado **crudPy**.

## 3. Verificar las carpetas creadas (`03_Creo_carpetas`)

Dentro de `Entornos\crudPy` deben aparecer: `Include`, `Lib`, `Scripts` y
`pyvenv.cfg`. Si estan, el entorno se creo bien.

## 4. Activar el entorno (`04_activar`)

```cmd
cd crudPy
cd Scripts
Activate
cd..
cd..
cd..
```

Al activarse, el prompt cambia a `(crudPy) D:\Curso_Phyton\00_BD_CRUD>`.
Los tres `cd..` te devuelven a la carpeta del proyecto.

## 5. Abrir Visual Studio Code (`05_Ir_visual_studio`)

```cmd
code .
```

Se abre VS Code en `00_BD_CRUD`, con el entorno ya activado.

## 6. Instalar el conector de MySQL (`06_Instala_mysql`)

```cmd
pip install mysql-connector-python
```

Debe terminar en `Successfully installed mysql-connector-python-9.7.0`.
El aviso de actualizar pip es opcional, se puede ignorar.

## 7. Permisos de PowerShell (`07_PowerShell`)

Solo si usas PowerShell (no hace falta en cmd) y te dice que la ejecucion de
scripts esta deshabilitada. Abre PowerShell **como administrador**:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Responde `S`. Es de una sola vez.

## 8. Escribir y ejecutar el CRUD (`08_Crud_py`)

El archivo `crud.py` de esta carpeta es la version completa: conexion, las
cuatro operaciones y un menu. Copialo a `D:\Curso_Phyton\00_BD_CRUD\crud.py`.

```cmd
python crud.py
```

| Opcion | Operacion | SQL      | Funcion              |
|--------|-----------|----------|----------------------|
| 1      | Create    | `INSERT` | `crear_alumno()`     |
| 2      | Read      | `SELECT` | `leer_alumnos()`     |
| 3      | Read      | `SELECT` | `buscar_alumno()`    |
| 4      | Update    | `UPDATE` | `actualizar_alumno()`|
| 5      | Delete    | `DELETE` | `eliminar_alumno()`  |

---

## Notas sobre tu codigo actual

- `import pyodbc` no se usa y puede dar error si no esta instalado: quitalo.
- Los `%s` de `cursor.execute(...)` no son formato de texto de Python, son
  marcadores del conector. Siempre pasa los valores en la tupla del segundo
  argumento (asi se evita la inyeccion SQL).
- Falta `conexion.commit()` despues de cada INSERT, UPDATE y DELETE; sin el,
  los cambios no se guardan.

## Errores mas comunes

- `ModuleNotFoundError: No module named 'mysql'` — no activaste el entorno
  (paso 4) o no instalaste el conector (paso 6).
- `Can't connect to MySQL server on '127.0.0.1:3306'` — MySQL esta en otro
  puerto: descomenta `port=3307` en `crud.py`, o enciende MySQL en XAMPP.
- `Unknown database 'matricula'` — el nombre de la base esta mal escrito.
- `Access denied for user 'root'@'localhost'` — revisa `password` (en XAMPP
  normalmente va vacio: `password=""`).
- `Duplicate entry 'ALU-001' for key 'PRIMARY'` — ese codigo ya existe, usa otro.
