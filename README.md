# CRUD Escolar con Python, SQLAlchemy y SQLite

Este proyecto es una aplicación CRUD (Crear, Leer, Actualizar, Eliminar) construida con **Python**, utilizando **SQLAlchemy** como ORM y **SQLite** como base de datos. La estructura del proyecto sigue el patrón de diseño **MVC (Modelo-Vista-Controlador)**.

## Estructura del Proyecto

```
crud_app/
├── main.py
├── db/
│   └── connection.py
└── core/
    ├── controllers.py
    ├── models.py
    └── views.py
```

## Descripción de la Aplicación

La aplicación permite gestionar:

* **Estudiantes**
* **Profesores**
* **Cursos**

### Relaciones:

* Un profesor puede impartir varios cursos (**1\:N**).
* Un curso puede tener varios estudiantes y un estudiante puede inscribirse en varios cursos (**N\:M**).

## Requisitos

* Python 3.10 o superior
* SQLAlchemy

### Instalación de dependencias

```bash
pip install sqlalchemy
```

## Uso

Ejecuta la aplicación desde `main.py`:

```bash
python main.py
```

### Funcionalidades:

1. Crear, ver, editar y eliminar **estudiantes**
2. Crear, ver, editar y eliminar **profesores**
3. Crear, ver, editar y eliminar **cursos**

Cada entidad se gestiona desde la consola a través de un menú interactivo.

## Base de Datos

El archivo de base de datos `crud_app.db` se genera automáticamente al ejecutar el programa por primera vez. Se encuentra en la raíz del proyecto.

## Autores

* Desarrollado por Alejandro Molina

## Licencia

Este proyecto está bajo la licencia MIT.
