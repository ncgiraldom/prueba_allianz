import pandas as pd
from pathlib import Path

def cargar_archivos_excel(ruta_directorio: str, patron_archivo: str = "*.xlsx") -> pd.DataFrame:
    """
    Carga todos los archivos Excel desde un directorio específico.
    
    Args:
        ruta_directorio (str): Ruta a la carpeta donde se encuentran los archivos.
        patron_archivo (str): Patrón para identificar archivos Excel (por defecto todos los .xlsx).
        
    Returns:
        pd.DataFrame: DataFrame concatenado con todos los archivos, incluyendo columna de 'mes'.
    """
    ruta = Path(ruta_directorio)
    archivos = list(ruta.glob(patron_archivo))
    
    if not archivos:
        raise FileNotFoundError(f"No se encontraron archivos en {ruta_directorio} con patrón {patron_archivo}")
    
    df_list = []
    for archivo in archivos:
        try:
            df = pd.read_excel(archivo, engine='openpyxl')
            df['mes'] = archivo.stem.split("_")[0]  # Extraer parte del nombre como mes
            df_list.append(df)
        except Exception as e:
            print(f"Error al leer {archivo.name}: {e}")
    
    df_total = pd.concat(df_list, ignore_index=True)
    print(f"Archivos cargados: {len(df_list)}")
    print(f"Registros totales: {df_total.shape[0]}")
    
    return df_total
