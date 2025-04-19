import pandas as pd

def format_columns(df: pd.DataFrame) -> pd.DataFrame:
    # Dates
    #df["fecha_registro"] = pd.to_datetime(df["fecha_registro"], utc=True, errors="coerce")
    #df["fecha_nacimiento"] = pd.to_datetime(df["fecha_nacimiento"], errors="coerce")
    #df["cotizacion_fecha"] = pd.to_datetime(df["cotizacion_fecha"], errors="coerce")

    # Float value
    if "valor_prima" in df.columns:
        df["valor_prima"] = (
            df["valor_prima"]
            .str.replace(",", ".", regex=False)
            .astype(float)
        )

    # Integers
    for col in ["edad", "valor_fasecolda", "modelo"]:
        if col in df.columns:
            df[col] = (
                df[col]
                .str.replace(",", "", regex=False)
                .astype(int)
            )

    # Text-based IDs to preserve formatting
    for col in ["comparison_id", "fasecolda_id", "dane_id", "departamento_id"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    # Booleans
    boolean_fields = {
        "rce_limite_unico": ["true", "false"],
        "emitido_cotizacion": ["true", "false"]
    }
    for col in boolean_fields:
        if col in df.columns:
            df[col] = df[col].str.lower().map({"true": True, "false": False})

    return df

def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    filter_class = df["clase"] == "AUTOMOVIL"
    filter_coverage = df["tipo_cobertura"] == "Todo_riesgo"
    filter_rce = df["rce"] == ">1500"
    return df[filter_class & filter_coverage & filter_rce].copy()

def clean_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans text columns in the DataFrame by removing spaces and stripping whitespace.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing text columns to clean.

    Returns:
    pd.DataFrame: A DataFrame with cleaned text columns.
    """
    text_columns = df.select_dtypes(include=['object', 'string']).columns
    for col in text_columns:
        df[col] = df[col].str.strip()
    return df.copy()
    
