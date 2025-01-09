# Usa una imagen base de Python 3.8
FROM python:3.8-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar nmap (binario) y otras herramientas necesarias
RUN apt-get update && apt-get install -y \
    nmap \
    && rm -rf /var/lib/apt/lists/*

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias del archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Instalar el paquete Python nmap explícitamente
RUN pip install python-nmap

# Exponer el puerto en el que se ejecutará la aplicación Flask
EXPOSE 5200

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
