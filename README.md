Proyecto Final "# Fake News Detector" 

---

## Integrantes del equipo

- Reychell Segura Fernández
- Ana María Ramírez Campabadal
- Gloria Mata Curling

Todos los integrantes figuran como **colaboradores** del repositorio.

---



# Fake News Detector - MLOps Project

## Descripción
Este proyecto implementa un sistema de detección de noticias falsas utilizando un modelo de Machine Learning. Se desarrolló siguiendo prácticas de MLOps para asegurar la automatización, versionamiento y despliegue continuo del modelo y la API.

El sistema incluye:
- Entrenamiento y reentrenamiento automatizado del modelo (`retrain.py`)
- Versionamiento de datos y modelos usando DVC
- Despliegue de una API REST utilizando **FastAPI**
- Contenedores Docker (`Dockerfile`, `docker-compose.yml`) para ejecución
- Integración continua con **GitHub Actions**

---
## Branches utilizados

- `main`
- `develop`
- `staging`

**Todas las ramas han sido conservadas** durante el proceso.

---

## Estructura principal del proyecto

- `main.py`: Archivo principal para ejecutar la API con FastAPI
- `retrain.py`: Script para reentrenar el modelo de noticias falsas
- `fake_news_classifier.joblib`: Modelo entrenado
- `models/`: Carpeta de utilitarios relacionados al modelo
- `app/`: Módulos de la API
- `download_fake_news.py`: Script para descarga de datos
- `fake_news_dataset_modified.csv`: Dataset modificado de noticias falsas

---

## Instrucciones de Ejecución

### Requerimientos
- Python 3.8 o superior
- Docker (opcional)
- DVC
- Git
- AWS CLI (opcional)

### Clonar el repositorio
```bash
git clone https://github.com/Rey0254/fake-news-detector-mlops.git
cd fake-news-detector-mlops
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Inicializar DVC y descargar datos
```bash
dvc pull
```

### Ejecutar la API localmente
```bash
uvicorn main:app --reload
```
La API estará disponible en: `http://127.0.0.1:8000`

---

## Documentación del modelo y API

### Inputs del modelo
- **text** (`string`): Texto de una noticia que se desea clasificar.

### Outputs del modelo
- **prediction** (`string`): Resultado `"FAKE"` o `"REAL"`.

### Endpoints principales

- `POST /predict`
  - **Request body**:
    ```json
    {
      "text": "Texto de la noticia a clasificar"
    }
    ```
  - **Respuesta**:
    ```json
    {
      "prediction": "FAKE"
    }
    ```

- `GET /`
  - Verifica que el servidor API esté activo.

---

## Ejecución usando Docker

### Build de la imagen Docker
```bash
docker build -t fake-news-detector .
```

### Correr el contenedor
```bash
docker run -p 8000:8000 fake-news-detector
```

Acceso a la API en: `http://localhost:8000`

### También puedes usar docker-compose
```bash
docker-compose up
```

---

## Reentrenar el modelo
Para reentrenar el modelo utilizando nuevos datos:
```bash
python retrain.py
```
Esto actualizará `fake_news_classifier.joblib`.

---

## Flujo de CI/CD

- **GitHub Actions** ejecuta pruebas automáticas, linting y chequeos de formato.
- **Docker** para contenerización de la API.
- **DVC** para versionamiento de datasets y modelo.
