import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

def imputar_perdida_total_cobertura(df, target='perdida_total_cobertura', features=None):
    """
    Imputa valores faltantes en una variable categórica dicotómica usando RandomForestClassifier.

    Parámetros:
    - df: DataFrame original
    - target: nombre de la variable categórica a imputar
    - features: lista de variables predictoras

    Retorna:
    - df con la columna imputada (conservando los valores originales no nulos)
    """
    df = df.copy()

    # Separar los datos disponibles y los faltantes
    df_known = df[df[target].notna()]
    df_missing = df[df[target].isna()]

    if df_missing.empty:
        return df

    # Definir variables de entrada
    if features is None:
        features = df.columns.drop([target])

    # Identificar tipos de variables
    cat_features = df[features].select_dtypes(include='object').columns.tolist()
    num_features = df[features].select_dtypes(include=['int64', 'float64']).columns.tolist()

    # Preprocesamiento: escalar numéricas y one-hot a categóricas
    transformer = ColumnTransformer([
        ("num", StandardScaler(), num_features),
        ("cat", OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_features)
    ])

    # Pipeline
    pipeline = Pipeline(steps=[
        ('preproc', transformer),
        ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    # Entrenar modelo
    X_train = df_known[features]
    y_train = df_known[target]
    pipeline.fit(X_train, y_train)

    # Predecir faltantes
    X_missing = df_missing[features]
    y_pred = pipeline.predict(X_missing)

    df.loc[df[target].isna(), target] = y_pred

    return df

import matplotlib.pyplot as plt
import seaborn as sns

def reporte_imputacion_distribucion(df_original, df_imputado, columna='perdida_total_cobertura'):
    """
    Compara la distribución de una variable categórica antes y después de imputación.
    
    Muestra gráficos de barras comparando las frecuencias relativas.
    """
    # Distribuciones relativas
    dist_original = df_original[columna].value_counts(normalize=True, dropna=False).rename("Antes imputación")
    dist_imputado = df_imputado[columna].value_counts(normalize=True).rename("Después imputación")

    # Unir para comparación
    df_comparacion = pd.concat([dist_original, dist_imputado], axis=1).fillna(0) * 100

    # Gráfico
    df_comparacion.plot(kind='bar', figsize=(8, 4))
    plt.title(f"📊 Comparación de distribución: {columna}")
    plt.ylabel("% del total")
    plt.xticks(rotation=0)
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

    return df_comparacion.round(2)
