import pandas as pd
import numpy as np


def analyze_csv(file):
    # Read CSV
    df = pd.read_csv(file, low_memory=False)

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