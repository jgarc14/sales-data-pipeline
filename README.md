# Sales Data Pipeline

Mini pipeline batch de procesamiento de datos construido con Python siguiendo principios de ingeniería de datos y buenas prácticas de software.

Este proyecto simula el procesamiento de datos de ventas, aplicando limpieza, validación y agregaciones analíticas, generando un dataset optimizado para consumo analítico.

---

## 📌 Objetivo

Construir un pipeline modular que:

- Extraiga datos desde un archivo CSV
- Limpie registros inválidos (montos negativos, productos nulos)
- Genere métricas agregadas por categoría
- Genere salida en formato analítico (Parquet)
- Incluya logging estructurado
- Incluya testing automatizado

---

## 🏗️ Arquitectura

El proyecto sigue una separación por capas tipo ETL:
```
src/
├── extract.py # Lectura de datos
├── transform.py # Limpieza y agregaciones
├── load.py # Escritura de resultados
├── config.py # Configuración de logging
└── main.py # Orquestación del pipeline
```

Principios aplicados:

- Separación de responsabilidades
- Funciones puras en la capa de transformación
- Logging estructurado en formato JSON
- Testing unitario con pytest
- Ejecución como módulo (`python -m`)

---

## 📊 Transformaciones implementadas

### Limpieza

- Eliminación de montos negativos
- Eliminación de productos nulos

### Agregaciones

Por categoría se calcula:

- `total_sales`
- `avg_sales`
- `total_orders`

---

## 📦 Formato de salida

El dataset final se genera en formato **Parquet**, formato columnar optimizado para:

- Motores analíticos
- Data Lakes
- Procesamiento distribuido (Spark)
- Consultas eficientes

---

## 🚀 Ejecución

1. Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependencias
```bash
pip install -r requirements.txt
```

3. Ejecutar pipeline
```bash
python3 -m src.main
```

## 🧪 Testing

El proyecto incluye pruebas unitarias para la capa de transformación.

Ejecutar:
```bash
pytest
```

## Stack Tecnológico

- Python 3.12
- Pandas
- PyArrow
- Pytest

## 🔎 Logging

El pipeline utiliza logging estructurado en formato JSON para facilitar:

- Observabilidad

- Integración con sistemas de monitoreo

- Trazabilidad en entornos productivos

Ejemplo de log:

```
{"time":"2026-03-01 14:49:48,234","level":"INFO","message":"Starting pipeline"}
```

### Posibles mejoras (Roadmap)

Este proyecto puede evolucionar hacia:

- Validación de esquema con Pydantic
- Manejo de errores más granular
- Orquestación con Airflow
- Migración a PySpark
- Ingesta desde base de datos
- Contenerización con Docker
- Integración con almacenamiento cloud (S3 / GCS)

## 🎯 Contexto

- Procesamiento batch
- Modelado analítico
- Arquitectura de datos escalable
- Observabilidad y confiabilidad de pipelines
