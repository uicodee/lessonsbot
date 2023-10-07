from aiogram import Router, types, F, Bot
from aiogram.filters import CommandStart

from keyboards.inline.category import category_keyboard

router = Router()


@router.message(CommandStart())
async def on_cmd_start(message: types.Message, bot: Bot) -> None:
    # users = [1498858629, 6659459993, 587676249]
    # print(message.from_user.id)
    # for user in users:
    #     await bot.send_message(
    #         chat_id=user,
    #         text="Reklama"
    #     )
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


# @router.message(F.content_type.in_({'text', 'sticker', 'photo'}))
# async def on_multimedia(message: types.Message) -> None:
#     await message.answer(
#         text="Men text, sticker yoki photo qabul qildim"
#     )
#
#
# @router.message(F.photo | F.video | F.sticker)
# async def on_multimedia(message: types.Message) -> None:
#     await message.answer(
#         text="Men text, sticker yoki photo qabul qildim"
#     )


@router.message(F.photo)
async def on_photo(message: types.Message, bot: Bot) -> None:
    print(message.photo[-1])
    await bot.download(
        message.photo[-1],
        destination=f"photos/{message.photo[-1].file_id}.jpg"
    )
