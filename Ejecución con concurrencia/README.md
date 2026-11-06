# Ejercicio 2: Ejecución con Concurrencia

## Descripción del Ejemplo (Vida Diaria)
Este script de Python simula a **dos usuarios entrenando en el gimnasio y compartiendo recursos de forma concurrente**:

- Cuando **Yo (Usuario 1)** termino una serie en el *Press de Banca*, entro en mi **tiempo muerto (descanso entre series)**. En lugar de bloquear la máquina sin hacer nada, paso a usar la **caminadora** durante mi descanso.
- Mientras estoy en la caminadora en ese tiempo muerto, el **Compañero (Usuario 2)** aprovecha para usar la misma máquina (*Press de Banca*) que dejé libre.
- Gracias a la **concurrencia** (`asyncio`), los tiempos de espera/descanso de un usuario son aprovechados por el otro usuario para avanzar en su entrenamiento, optimizando el uso de los recursos del gimnasio y reduciendo el tiempo total.

## Estructura del Proyecto
- `02_concurrente.py`: Script de Python con `asyncio` que visualiza la concurrencia entre los dos usuarios.
- `docker-compose.yml`: Configuración del contenedor de Docker.
- `README.md`: Instrucciones de ejecución.

## Cómo ejecutar el script con Docker

### Opción 1: Usando Docker Compose 
1. Abre una terminal y entra en la carpeta del ejercicio:
   ```bash
   cd "Ejecución con concurrencia"
   ```
2. Ejecuta el contenedor con Docker Compose:
   ```bash
   docker compose up
   ```
3. Para limpiar el contenedor al finalizar:
   ```bash
   docker compose down
   ```

### Opción 2: Usando comando `docker run` directamente
```bash
docker run --rm -v "${PWD}:/app" -w /app python:3.11.18-slim-trixie python -u 02_concurrente.py
```
