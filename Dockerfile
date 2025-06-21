# Imagen base oficial (ligera)
FROM python:3.11-slim

# Crea carpeta de trabajo
WORKDIR /app

# Copia dependencias primero
COPY requirements.txt .

# Instala dependencias
RUN pip install -r requirements.txt

# Copia el resto del código
COPY . .

# Expón el puerto en el que corre Flask (por defecto 5000)
EXPOSE 5000

# Arranca la aplicación
CMD ["python", "app.py"]
