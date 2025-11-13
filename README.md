# 🐾 VetCare – Sistema de Gestión Veterinaria
**VetCare** es una aplicación web desarrollada con **Python + Django + Bootstrap 5**, diseñada para administrar **dueños, mascotas y visitas veterinarias** desde una interfaz moderna, profesional y completamente responsive.

## 🎥 Demo
> 📁 La carpeta VetcareDemo/ contiene imágenes del funcionamiento del sistema.

## 🚀 Características principales
- **CRUD completo** de Dueños, Mascotas y Visitas.
- **Interfaz moderna** con diseño oscuro tipo *Unity UI*.
- Formularios con estilo **Pupassure** (imagen lateral + campos limpios).
- **API REST** integrada con *Django REST Framework*.
- Sistema escalable preparado para módulos futuros (por ejemplo, *Servicios* o *Pagos*).
- **Base de datos SQLite** por defecto (fácil de migrar a PostgreSQL o MySQL).

## 🧩 Estructura del proyecto
ABM_Veterinaria/
│
├── mascotas/ # App principal (modelos, vistas, urls, forms)
│ ├── templates/ # Templates HTML
│ ├── static/css/ # Archivos CSS personalizados
│ ├── views.py # Lógica del CRUD y API
│ ├── models.py # Estructura de datos (Dueño, Mascota, Visita)
│ ├── forms.py # Formularios personalizados
│ └── serializers.py # API REST (Django REST Framework)
│
├── veterinaria/ # Configuración principal de Django
│ └── urls.py # Rutas globales del proyecto
│
├── VetcareDemo/ # 🎥 Carpeta con demo visual
│
├── manage.py
└── requirements.txt

## ⚙️ Instalación y ejecución
1. **Clonar el repositorio**
En cmd:
git clone https://github.com/HesellGOD/ABM_Veterinaria.git
cd ABM_Veterinaria

2. **Crear y activar el entorno virtual**
En cmd:
python -m venv venv
source venv/Scripts/activate     # En Windows
source venv/bin/activate         # En Linux/Mac

3. **Instalar dependencias**
En cmd:
pip install -r requirements.txt

4. **Ejecutar migraciones**
en cmd:
python manage.py migrate

5. **Iniciar el servidor**
python manage.py runserver

6. **Abrir en el navegador**
http://127.0.0.1:8000/

🧠 Stack Tecnológico
Backend: Python, Django
Frontend: HTML5, CSS3, Bootstrap 5
API: Django REST Framework
Base de datos: SQLite (por defecto)
Control de versiones: Git / GitHub

🧑‍💻 Desarrollador
👨‍💻 Hesel Eduardo Cornejo
📍 Los Cerrillos, Córdoba – Argentina
📧 cornejoheselleduardo@gmail.com
🌐 LinkedIn
💻 GitHub

🐍 Próximas mejoras
 Módulo Servicios (vacunación, esterilización, peluquería, etc.)