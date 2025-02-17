from aiogram.utils.formatting import Text, Bold
from aiogram import Router, types
from aiogram.filters import CommandStart, Command

from app.commands import BOT_COMMANDS_STR
from app.users.dependencies import UserServiceDep
from app.users.keyboards import MAIN_MENU_KB

router = Router()


@router.message(CommandStart())
async def start_command(message: types.Message, users: UserServiceDep) -> None:
    assert message.from_user
    user = await users.get_by_telegram_id(message.from_user.id)
    if user:
        await message.answer(
            f"Добро пожаловать, {user.display_name}! 😊",
            reply_markup=MAIN_MENU_KB,
        )
    else:
        user = await users.register(
            telegram_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
        await message.answer(
            f"Добро пожаловать, {user.display_name}! "
            "Я помогаю тестировщикам организовывать задачи проекта. Давай приступим к работе! 😊",
            reply_markup=MAIN_MENU_KB,
        )


@router.message(Command("help"))
async def get_help(message: types.Message) -> None:
    await message.answer("**Навигация по боту**:\n\n" + BOT_COMMANDS_STR)


@router.message(Command("about"))
async def about(message: types.Message) -> None:
    authors = [
        "@ivanstasevich",
        "@ApexBis",
        "@Dmitry_Skarga",
        "@midnightknight",
    ]
    text = Text(
        "Бот разработан в рамках хакатона ",
        Bold("Студент года IT 2023\n\n"),
        "Команда: " + " ".join(authors),
    )
    await message.answer(text.as_markdown())
