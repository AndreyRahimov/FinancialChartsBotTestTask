from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from database.company_names import get_company_names


def make_company_keyboard(file_path: str) -> ReplyKeyboardMarkup | None:
    companies = get_company_names(file_path)

    if companies:
        buttons = [KeyboardButton(text=company) for company in companies]
        company_kb_builder = ReplyKeyboardBuilder()
        company_kb_builder.row(*buttons, width=2)

        return company_kb_builder.as_markup(resize_keyboard=True)


income_buton = KeyboardButton(text="доход компании")
expense_buton = KeyboardButton(text="расход компании")
profit_buton = KeyboardButton(text="прибыль компании")
tax_buton = KeyboardButton(text="КПН компании")

financial_data_builder = ReplyKeyboardBuilder()
financial_data_builder.row(
    income_buton, expense_buton, profit_buton, tax_buton, width=2
)

financial_data_kb = financial_data_builder.as_markup(resize_keyboard=True)
