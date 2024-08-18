from environs import Env
from pprint import pprint

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def get_company_data(file_path: str, company: str) -> pd.DataFrame | None:
    try:
        return pd.read_excel(file_path, sheet_name=company)
    except ValueError:
        return


def create_chart(company: str, data_type: str, user_id: int) -> None:
    env: Env = Env()
    env.read_env()

    df = get_company_data(env("DATABASE"), company)

    column_names = list(df.columns)
    column = None

    for column_name in column_names:
        if column_name.lower().startswith(data_type.lower()):
            currency = column_name.strip()[-2]
            column = column_name
            break

    if column:
        df["Месяц"] = df["Месяц"].apply(str.strip)

        plt.figure(figsize=(10, 6))
        sns.lineplot(x="Месяц", y=column, data=df, marker="o")

        plt.title(f"Информация о компании {company}")
        plt.xlabel("Месяц")
        plt.ylabel(f"{data_type}, {currency}")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.savefig(f"{user_id}.png")


create_chart("Onix Corp.", "Прибыль", 784846420)
