from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


@router.message()
async def send_answer(message: Message):
    await message.answer(
        text=LEXICON_RU["other answer"], reply_markup=ReplyKeyboardRemove()
    )
