🗃️ Estructura del Proyecto
edgar/                   # Proyecto Django principal
│
├── edgar/               # Configuración global
│   └── settings.py      # Configuración del proyecto
│
├── patinoApp/           # Aplicación funcional principal
│   ├── models.py        # Modelado de datos
│   ├── views.py         # Lógica de negocio (CRUD)
│   ├── urls.py          # Rutas de la app
│   ├── templates/
│   │   └── html/        # Archivos HTML
│   └── static/
│       └── js/          # Archivos JS
│       └── css/         # Archivos CSS
│
├── user/                # Aplicación para override de usuario
│   ├── models.py        # User personalizado
│   ├── admin.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
└── manage.py

🔐 Autenticación
Override del modelo de usuario: Se crea un modelo User personalizado usando AbstractUser dentro de la app user.

Se registran  2 usuarios 
admin2
admin3

📊 Modelado de Datos
Paciente: nombre, email.

Cita: fecha, descripción, relacionada con Paciente.

🧮 CRUD Implementado
CRUD completo para el modelo Paciente

CRUD completo para el modelo Cita

Uso de clases basadas en vistas (ListView, CreateView, etc.)

Formularios renderizados automáticamente con {{ form.as_p }}

🌐 Navegación y URLs
URLs configuradas para:

/ Lista de pacientes

/nuevo/ Crear paciente

/editar/<id>/ Editar paciente

/eliminar/<id>/ Eliminar paciente

citas/ para manejar Cita

🎨 Frontend
Uso de plantilla base: base.html

CSS personalizado ubicado en static/css/estilos.css

Animaciones y comportamiento dinámico con JS desde static/js/scripts.js

Todas las plantillas heredan de base.html

Ejemplo de animaciones:

Cambio de estilo al hacer hover o click en botón

Alerta con alert('Mensaje') al hacer clic en botón

📁 Archivos estáticos y plantilla
static/ contiene CSS y JS

templates/html/ contiene los archivos .html

Se usa {% static %} para incluir correctamente recursos

{% load static %} presente en base.html


