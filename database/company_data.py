import pandas as pd


def get_company_data(file_path: str, company: str) -> pd.DataFrame | None:
    try:
        return pd.read_excel(file_path, sheet_name=company)
    except ValueError:
        return
