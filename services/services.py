from environs import Env

import matplotlib.pyplot as plt
import seaborn as sns

from database.company_data import get_company_data


def create_chart(company: str, data_type: str, user_id: int) -> None:
    env: Env = Env()
    env.read_env()
    df = get_company_data(env("DATABASE"), company)

    data_type = data_type.split()[0]

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
        plt.ylabel(f"{data_type.upper()}, {currency}")
        plt.xticks(rotation=45)
        plt.grid(True)
        print("save chart")
        plt.savefig(f"{user_id}.png")
