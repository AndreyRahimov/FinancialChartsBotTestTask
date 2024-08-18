from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    FSInputFile,
    Message,
    ReplyKeyboardRemove,
)

from filters.is_company_name import IsCompanyName
from keyboards.keyboards import financial_data_kb, make_company_keyboard
from lexicon.lexicon_ru import LEXICON_RU
from services.services import create_chart


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message, database) -> None:
    companies_kb = make_company_keyboard(database)
    if companies_kb:
        await message.answer(text=LEXICON_RU["/start"], reply_markup=companies_kb)
    else:
        await message.answer(text=LEXICON_RU["no companies"])


@router.message(IsCompanyName())
async def process_company_button(message: Message, users) -> None:
    user_id = message.from_user.id
    if user_id not in users:
        users[user_id] = {}
    users[user_id]["company"] = message.text
    await message.answer(
        text=LEXICON_RU["company choice"],
        reply_markup=financial_data_kb,
    )


@router.message(
    F.text.in_(
        {"доход компании", "расход компании", "прибыль компании", "КПН компании"}
    )
)
async def process_data_type_button(message: Message, bot, users) -> None:
    user_id = message.from_user.id

    try:
        company = users[user_id]["company"]

    except KeyError:
        await message.answer(
            text=LEXICON_RU["error"],
            reply_markup=ReplyKeyboardRemove(),
        )

    create_chart(company=company, data_type=message.text, user_id=user_id)
    users[user_id]["company"] = None
    photo_path = f"{user_id}.png"
    photo = FSInputFile(photo_path)

    await message.answer_photo(
        photo=photo,
        caption=LEXICON_RU["send photo"],
        reply_markup=ReplyKeyboardRemove(),
    )

    await message.answer(text=LEXICON_RU["launch"])


@router.message(Command(commands="help"))
async def process_help_command(message: Message) -> None:
    await message.answer(text=LEXICON_RU["/help"], reply_markup=ReplyKeyboardRemove())
