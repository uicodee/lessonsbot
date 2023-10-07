from aiogram import Router, types, F, Bot
from aiogram.filters import CommandStart

from keyboards.inline.category import category_keyboard

router = Router()


@router.message(CommandStart())
async def on_cmd_start(message: types.Message, bot: Bot) -> None:
    print(message.from_user.id)
    users = [1731595218, 6140087280, 5103930673, 2147475522]
    # print(message.from_user.id)
    for user in users:
        await bot.send_message(
            chat_id=user,
            text="Reklama"
        )
    await message.answer(
        text=f"Assalomu alaykum, {message.from_user.full_name}\n"
             f"Kerakli kategoriyani tanlang",
        reply_markup=category_keyboard()
    )
    # await bot.send_message(
    #     chat_id=6659459993,
    #     text=f"Assalomu alaykum, {message.from_user.full_name}\n"
    #          f"Kerakli kategoriyani tanlang",
    #     reply_markup=category_keyboard()
    # )


@router.message(F.video)
async def on_video(message: types.Message) -> None:
    await message.answer(text=message.video.file_id)


@router.message(F.photo)
async def on_video(message: types.Message) -> None:
    await message.answer(text=message.photo[-1].file_id)


# @router.message(F.content_type.in_({'text', 'sticker', 'photo'}))
# async def on_multimedia(message: types.Message) -> None:
#     await message.answer(
#         text="Men text, sticker yoki photo qabul qildim"
#     )
#
#
# @router.message(F.photo | F.video | F.sticker | F.animation)
# async def on_multimedia(message: types.Message) -> None:
#     await message.answer(
#         text="Men text, sticker yoki photo qabul qildim"
#     )
# [
#     PhotoSize(file_id='AgACAgIAAxkBAAIC6WUhLhEEOTDUqUkGb0Rrlc6lZxfUAALezDEbJXMRSYYF1TwTqUzCAQADAgADcwADMAQ', file_unique_id='AQAD3swxGyVzEUl4', width=90, height=54, file_size=938),
#     PhotoSize(file_id='AgACAgIAAxkBAAIC6WUhLhEEOTDUqUkGb0Rrlc6lZxfUAALezDEbJXMRSYYF1TwTqUzCAQADAgADbQADMAQ', file_unique_id='AQAD3swxGyVzEUly', width=320, height=192, file_size=11657),
#     PhotoSize(file_id='AgACAgIAAxkBAAIC6WUhLhEEOTDUqUkGb0Rrlc6lZxfUAALezDEbJXMRSYYF1TwTqUzCAQADAgADeAADMAQ', file_unique_id='AQAD3swxGyVzEUl9', width=800, height=480, file_size=48169),
#     PhotoSize(file_id='AgACAgIAAxkBAAIC6WUhLhEEOTDUqUkGb0Rrlc6lZxfUAALezDEbJXMRSYYF1TwTqUzCAQADAgADeQADMAQ', file_unique_id='AQAD3swxGyVzEUl-', width=1000, height=600, file_size=49031)
# ]

@router.message(F.photo)
async def on_photo(message: types.Message, bot: Bot) -> None:
    print(message.photo[-1])
    await bot.download(
        message.photo[-1],
        destination=f"photos/{message.photo[-1].file_id}.jpg"
    )
