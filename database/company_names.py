from typing import KeysView

import pandas as pd


def get_company_names(file_path: str) -> KeysView[str] | None:
    excel_data = pd.read_excel(file_path, sheet_name=None)

    return excel_data.keys() if excel_data else None
