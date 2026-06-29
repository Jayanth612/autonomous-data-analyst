from app.services import data_loader


from app.services import data_loader

COLUMN_ALIASES = {
    "sales": [
        "sales",
        "revenue",
        "amount",
        "total sales"
    ],

    "product": [
        "product",
        "product name",
        "item",
        "product category"
    ],

    "region": [
        "region",
        "location",
        "country",
        "city",
        "market"
    ],

    "date": [
        "date",
        "order date",
        "purchase date"
    ]
}


def find_column(column_type):
    df = data_loader.df_global

    if df is None:
        return None

    aliases = COLUMN_ALIASES.get(column_type.lower(), [])

    for column in df.columns:
        column_lower = column.lower()

        for alias in aliases:
            if alias in column_lower:
                return column

    return None


def sales_by_region():
    df = data_loader.df_global

    sales_col = find_column("sales")
    region_col = find_column("region")

    if sales_col is None or region_col is None:
        return {
            "message": "Sales or Region column not found."
        }

    result = (
        df.groupby(region_col)[sales_col]
        .sum()
        .sort_values(ascending=False)
    )

    return result.to_dict()


def sales_by_product():
    df = data_loader.df_global

    sales_col = find_column("sales")
    product_col = find_column("product")

    if sales_col is None or product_col is None:
        return {
            "message": "Sales or Product column not found."
        }

    result = (
        df.groupby(product_col)[sales_col]
        .sum()
        .sort_values(ascending=False)
    )

    return result.to_dict()
    
    

def sales_by_product_and_region():
    df = data_loader.df_global

    sales_col = find_column("sales")
    product_col = find_column("product")
    region_col = find_column("region")

    if not sales_col or not product_col or not region_col:
        return {
            "message": "Required columns not found."
        }

    result = (
        df.groupby([product_col, region_col])[sales_col]
        .sum()
        .reset_index()
    )

    return result.to_dict(orient="records")