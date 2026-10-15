Proyecto Python: Gestión de libros y cálculo de rutas
Descripción
Este proyecto contiene dos scripts de Python que utilizan API externas para automatizar tareas:

Gestión de libros: genera 50 libros ficticios utilizando la biblioteca Faker y los registra mediante una API REST.
Cálculo de rutas: obtiene las coordenadas geográficas de dos lugares mediante la API de GraphHopper y calcula la distancia, el tiempo estimado de viaje en automóvil y las instrucciones de navegación.
Requisitos
Python 3.8 o superior.
Conexión a Internet.
Acceso a la API de la biblioteca, si se ejecuta el script de libros.
Una clave API válida de GraphHopper para el script de rutas.
Instalación
Clona el repositorio:
   git clone URL_DE_TU_REPOSITORIO
   cd NOMBRE_DEL_REPOSITORIO
Crea un entorno virtual:
   python -m venv venv
Activa el entorno virtual.
En Linux o macOS:

   source venv/bin/activate
En Windows:

   venv\Scripts\activate
Instala las dependencias:
   pip install requests Faker
Ejecución de los scripts
1. Generar libros ficticios
Guarda el primer script en un archivo llamado generar_libros.py.

Ejecuta:

python generar_libros.py
El programa se autentica con la API de la biblioteca y genera 50 libros con títulos, autores e ISBN aleatorios. Después, intenta registrar cada libro mediante solicitudes HTTP.

Importante: la API de la biblioteca debe estar disponible y las credenciales y claves de acceso deben ser válidas.

2. Calcular rutas entre dos lugares
Guarda el segundo script en un archivo llamado calcular_rutas.py.

Ejecuta:

python calcular_rutas.py
El programa solicitará el lugar de origen y el destino. A continuación, mostrará la distancia en kilómetros, el tiempo estimado en minutos y las instrucciones de navegación.

Para salir, escribe s o salir cuando el programa solicite un lugar.

Importante: debes configurar una clave API válida de GraphHopper antes de ejecutar el script.

Dependencias
requests: realiza solicitudes HTTP a las API.
Faker: genera datos ficticios para los libros.
json: procesa los datos JSON utilizados por la API de la biblioteca.
urllib.parse: módulo estándar de Python para trabajar con URL.
Seguridad
No publiques credenciales, contraseñas ni claves API en el repositorio. Guárdalas en variables de entorno y evita incluirlas directamente en el código fuente.

Autor
Proyecto de práctica de programación en Python e integración con API REST.****
