from app.services import data_loader
from app.services.query_engine import sales_by_region, sales_by_product

def analyze_question(question: str):
    if data_loader.df_global is None:
        return {
            "message": "No dataset uploaded."
        }

    sales_column = None

    for column in data_loader.df_global.columns:
        if column.lower() == "sales":
            sales_column = column
            break

    if sales_column is None:
        return {
            "message": "Sales column not found."
        }

    question = question.lower()

    if "total" in question:
        return {
            "answer": float(data_loader.df_global[sales_column].sum())
        }

    elif "average" in question or "mean" in question:
        return {
            "answer": float(data_loader.df_global[sales_column].mean())
        }

    elif "maximum" in question or "highest" in question or "max" in question:
        return {
            "answer": float(data_loader.df_global[sales_column].max())
        }

    elif "minimum" in question or "lowest" in question or "min" in question:
        return {
            "answer": float(data_loader.df_global[sales_column].min())
        }
    
    elif "region" in question:
        return sales_by_region()
    
    elif "product" in question:
        return sales_by_product()
    return {
        "message": "I don't understand that question yet."
    }