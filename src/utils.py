from pathlib import Path
import pandas as pd

def load_excel_files(directory: str, pattern: str = "*.xlsx") -> pd.DataFrame:
    """
    Loads and concatenates Excel files from a directory with all data as strings.
    """
    path = Path(directory)
    files = list(path.glob(pattern))

    if not files:
        raise FileNotFoundError(f"No Excel files found in {directory}")

    df_list = []
    for file in files:
        try:
            df = pd.read_excel(file, engine="openpyxl", dtype=str)
            df["source_file"] = file.stem.split("_")[0]
            df_list.append(df)
        except Exception as e:
            print(f"Error loading {file.name}: {e}")

    df_all = pd.concat(df_list, ignore_index=True)

    # Normalize column names
    df_all.columns = (
        df_all.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w\s]", "", regex=True)
    )

    return df_all
