import app.services.data_loader as data_loader


def analyze_sales():
    if data_loader.df_global is None:
        return {
            "message": "No dataset uploaded."
        }

    # Find the sales column
    sales_column = None

    for column in data_loader.df_global.columns:
        if column.lower() == "sales":
            sales_column = column
            break

    if sales_column is None:
        return {
            "message": "Sales column not found."
        }

    return {
        "total_sales": float(data_loader.df_global[sales_column].sum()),
        "average_sales": float(data_loader.df_global[sales_column].mean()),
        "maximum_sales": float(data_loader.df_global[sales_column].max()),
        "minimum_sales": float(data_loader.df_global[sales_column].min())
    }