Proyecto Final "# Fake News Detector" 

Integrantes:

Gloria Mata Curling
Ana Maria Ramirez Campabadal
Reychell Segura Fernandez

Todos los integrantes figuran como **colaboradores** en este repositorio.


# Fake News Detector - MLOps Project

## Descripción
Este proyecto implementa un sistema de detección de noticias falsas utilizando un modelo de Machine Learning. Se desarrolló siguiendo prácticas de MLOps para asegurar la automatización, versionamiento y despliegue continuo del modelo y la API.

El sistema incluye:
- **Entrenamiento y reentrenamiento automatizado del modelo**
- **Versionamiento de datos y modelo usando DVC**
- **Despliegue de una API REST (FastAPI) para hacer inferencias**
- **Contenedores Docker para ejecutar el sistema**
- **Integración y entrega continua con GitHub Actions**
- **Interfaz gráfica o API de predicción**

---

## Branches utilizados

Durante el desarrollo del proyecto, se utilizaron las siguientes ramas:

- `main`
- `develop`
- `staging`

Todas las ramas utilizadas en el proceso de desarrollo han sido mantenidas y no eliminadas.

---

## Instrucciones de Ejecución

### Requerimientos
- Python 3.8 o superior
- Docker
- DVC
- Git
- AWS CLI configurado (opcional para DVC remote en la nube)

### Clonar el repositorio
```
git clone https://github.com/Rey0254/fake-news-detector-mlops.git
cd fake-news-detector-mlops
```

### Instalar dependencias
```
pip install -r requirements.txt
```

### Inicializar DVC
```
dvc pull
```
*(Esto descarga los datos versionados del almacenamiento remoto configurado.)*

### Ejecutar la API localmente
```
uvicorn app.main:app --reload
```
Esto levanta la API en `http://127.0.0.1:8000`

---

## Documentación del modelo y API

### Inputs del modelo
- **Texto de noticia** (`string`): El texto completo o fragmento de la noticia a evaluar.

### Outputs del modelo
- **Clasificación** (`string`): Retorna `"FAKE"` o `"REAL"` dependiendo de la predicción del modelo.

### Endpoints principales de la API

- `POST /predict`
  - **Descripción**: Permite enviar un texto de noticia para clasificarlo como `FAKE` o `REAL`.
  - **Body de entrada (JSON)**:
    ```json
    {
      "text": "Aquí va el texto de la noticia"
    }
    ```
  - **Respuesta**:
    ```json
    {
      "prediction": "FAKE"
    }
    ```

- `GET /`
  - **Descripción**: Endpoint raíz que verifica que la API esté en funcionamiento.
 
  - ### Si se usa Interfaz Gráfica (ej. Streamlit)

- Para correr la interfaz:
  ```bash
  streamlit run app/streamlit_app.py
  ```
- Inputs:
  - Un campo de texto donde se pega la noticia.
- Outputs:
  - Un resultado visual indicando si la noticia es `FAKE` o `REAL`.

---

## Ejecución con Docker

**Construir la imagen Docker:**
```bash
docker build -t fake-news-detector .
```

**Correr el contenedor:**
```bash
docker run -p 8000:8000 fake-news-detector
```

La API estará disponible en `http://localhost:8000`.

---

## Flujo de CI/CD

- **Linting** y **testing automático** mediante **GitHub Actions** al hacer push a `develop`, `staging` o `main`.
- **Despliegue** usando contenedores Docker.
- **Control de versiones de datos y modelos** usando **DVC** conectado a almacenamiento remoto.
