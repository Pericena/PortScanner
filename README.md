# PortScanner - Análisis de Vulnerabilidades con Inteligencia Artificial

Bienvenido a **PortScanner**, una herramienta de análisis de vulnerabilidades de puertos desarrollada en Python con Flask, integrada con tecnologías avanzadas como OpenAI y Nmap. Este sistema web está diseñado para realizar escaneos profundos de puertos, identificar posibles vulnerabilidades, y generar reportes detallados. Funciona en Windows, Linux y Termux.

## Características Principales

- **Inteligencia Artificial**: Uso de OpenAI para analizar y clasificar las vulnerabilidades detectadas.
- **Integración con Nmap**: Escaneos potentes y fiables.
- **Compatibilidad Multiplataforma**: Funciona en Windows, Linux y Termux.
- **Sistema Web Interactivo**: Interfaz amigable y fácil de usar.
- **Reportes Detallados**: Generación de reportes en tiempo real con gráficos y análisis.
- **Código Abierto**: Totalmente gratuito y accesible.

---

## Capturas de Pantalla

### Panel Principal
![Captura de la Interfaz Principal](https://via.placeholder.com/800x400?text=Captura+de+Interfaz+Principal)

### Reporte de Vulnerabilidades
![Reporte de Vulnerabilidades](https://via.placeholder.com/800x400?text=Reporte+de+Vulnerabilidades)

### Escaneo en Proceso
![Escaneo en Proceso](https://via.placeholder.com/800x400?text=Escaneo+en+Proceso)

---

## Instalación

### Requisitos Previos
1. Python 3.8 o superior
2. Flask
3. Nmap instalado en el sistema
4. Acceso a internet para utilizar OpenAI

### Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Pericena/PortScanner.git
   cd PortScanner
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

   Asegúrate de que `requirements.txt` incluye lo siguiente:
   ```text
   Flask
   nmap
   openai
   pyyaml
   ```

3. Configura las credenciales de OpenAI:
   - Crea un archivo `.env` en el directorio raíz.
   - Añade tu clave de API de OpenAI:
     ```
     OPENAI_API_KEY=tu_clave_api
     ```

4. Inicia el servidor:
   ```bash
   python app.py
   ```

5. Accede a la aplicación desde tu navegador en [http://localhost:5000](http://localhost:5000).

---

## Uso

1. Selecciona el rango de IP o dominio a analizar.
2. Configura las opciones de escaneo (puertos específicos, velocidad, etc.).
3. Ejecuta el escaneo y revisa los resultados.
4. Genera reportes detallados con un clic.

---

## Contribución

¡Tu ayuda es bienvenida! Si encuentras un problema, abre un issue o envía un pull request.

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad:
   ```bash
   git checkout -b mi-nueva-funcionalidad
   ```
3. Realiza los cambios y haz un commit:
   ```bash
   git commit -m "Añadida nueva funcionalidad"
   ```
4. Envía los cambios:
   ```bash
   git push origin mi-nueva-funcionalidad
   ```
5. Abre un pull request en GitHub.

---

## Redes Sociales

- **Blog**: [lpericena.blogspot.com](https://lpericena.blogspot.com)
- **GitHub**: [Pericena](https://github.com/Pericena)
- **Twitter**: [@LuishinioP](https://twitter.com/LuishinioP)

---

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## Apoya el Proyecto

- Dale una ⭐ al repositorio para apoyar este proyecto.
- ¡Comparte con otros interesados en ciberseguridad y análisis de vulnerabilidades!

---

## Video de Demostración

[![Video de Demostración](https://via.placeholder.com/800x400?text=Captura+de+Video)](https://www.youtube.com/watch?v=demo)

---

## Agradecimientos

Agradecemos a la comunidad de ciberseguridad y desarrolladores por el soporte continuo en herramientas de código abierto.

