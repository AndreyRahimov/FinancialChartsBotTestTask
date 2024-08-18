from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database: str


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str | None = None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env("BOT_TOKEN"), admin_ids=list(map(int, env.list("ADMIN_IDS")))
        ),
        db=DatabaseConfig(
            database=env("DATABASE"),
        ),
    )
