import pandas as pd
import numpy as np

df_global = None


def analyze_csv(file):
    global df_global

    # Read CSV
    df = pd.read_csv(file, low_memory=False)

    # Store dataframe globally
    df_global = df

    # Missing values
    missing_values_dict = {
        col: int(val)
        for col, val in df.isnull().sum().items()
    }

    # Preview data
    preview_df = df.head().replace({
        np.nan: None,
        np.inf: None,
        -np.inf: None
    })

    # Return summary
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),

        "data_types": {
            col: str(dtype)
            for col, dtype in df.dtypes.items()
        },

        "missing_values": missing_values_dict,

        "preview": preview_df.to_dict(orient="records")
    }


def get_dataframe_summary():
    global df_global

    if df_global is None:
        return {
            "message": "No CSV uploaded yet."
        }

    return {
        "rows": len(df_global),
        "columns": len(df_global.columns),
        "column_names": df_global.columns.tolist(),

        "data_types": {
            col: str(dtype)
            for col, dtype in df_global.dtypes.items()
        },

        "missing_values": {
            col: int(val)
            for col, val in df_global.isnull().sum().items()
        },

        "statistics": df_global.describe(include="all").fillna("").to_dict()
    }