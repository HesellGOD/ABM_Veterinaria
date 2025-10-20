# 🐾 Veterinaria Django CRUD

Sistema web de gestión veterinaria desarrollado con **Python + Django + Django REST Framework**.

Permite administrar dueños, mascotas y visitas médicas, con soporte para API REST.

---

## 🚀 Tecnologías
- Python 3.10+
- Django 5.x
- Django REST Framework
- SQLite (local) / PostgreSQL (para producción)
- HTML5 / CSS3 (interfaz básica)

---

## 📦 Instalación local

```bash
# Clonar el repositorio
git clone https://github.com/HesellGOD/veterinaria_django_crud.git
cd veterinaria_django_crud

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver

Luego ingresá a http://127.0.0.1:8000/admin/

🧩 Endpoints API REST

Recurso	    URL	Métodos
Dueños	    /api/dueños/	GET, POST, PUT, DELETE
Mascotas	/api/mascotas/	GET, POST, PUT, DELETE
Visitas     /api/visitas/   GET, POST, PUT, DELETE

📚 Próximos pasos

Integrar almacenamiento de imágenes en AWS S3

Migrar base de datos a AWS RDS

Añadir módulo de análisis de texto con IA (Amazon Comprehend)

👨‍💻 Autor

[Cornejo Hesel Eduardo]
Desarrollador Python/Django | Cloud AWS | AI Integrations
LinkedIn | GitHub