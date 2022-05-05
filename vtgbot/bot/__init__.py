from vtgbot.misc import bot, dp, db
from vtgbot.log import logger
import aiogram
from aiogram.types import ContentType, BotCommand
from .handlers import start, handle_video


async def starter(*args, **kwargs):
    await bot.set_my_commands(
        commands=[
            BotCommand(
                command="start",
                description="Start"
            )
        ]
    )

    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(handle_video, content_types=ContentType.ANY)

    await bot.send_message(704477361, "Bot started")


async def shutdown(*args, **kwargs):
    db.db.commit()
    db.db.close()


def run():
    logger.info("Starting pooling")
    aiogram.executor.start_polling(dp, skip_updates=True, on_startup=starter, on_shutdown=shutdown)
