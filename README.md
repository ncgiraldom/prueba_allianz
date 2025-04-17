# Prueba Técnica - Científico de Datos en Aseguradora

Este repositorio contiene el desarrollo de la prueba técnica para el cargo de Científico de Datos. Se trabajó sobre un set de datos de cotizaciones del mercado asegurador ficticio con el objetivo de realizar análisis exploratorio y construir un modelo predictivo.

## 🧠 Objetivos

1. **Unificación y limpieza** de los datos de cotización de productos de autos.
2. **Análisis exploratorio (EDA)** de productos Todo Riesgo y RCE > 1500.
3. **Desarrollo de un modelo predictivo**, con posibilidad de escoger entre:
   - Modelo de **predicción de compra**.
   - Modelo de **competitividad** de ofertas.

## 📁 Estructura del proyecto

```bash
nombre-del-proyecto/
│
├── data/
│   ├── raw/               # Archivos Excel originales (no incluidos en el repo)
│   ├── processed/         # Datos limpios y combinados
│
├── notebooks/
│   ├── 01_eda.ipynb       # Exploración de datos
│   ├── 02_modelo.ipynb    # Desarrollo y evaluación del modelo
│
├── src/
│   ├── utils.py           # Funciones auxiliares para carga y limpieza
│   ├── preprocessing.py   # Transformaciones
│   ├── model.py           # Entrenamiento y evaluación de modelo
│
├── outputs/
│   ├── graficos/          # Visualizaciones generadas
│   ├── resultados/        # Resultados del análisis/modelo
│
├── models/                # Modelos guardados (pkl, joblib)
│
├── presentation/
│   ├── presentacion.pptx  # Diapositivas
│
├── requirements.txt       # Dependencias del proyecto
├── .gitignore             # Exclusiones para control de versiones
└── README.md              # Documentación del proyecto
