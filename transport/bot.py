from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from transport.filters import AdminFilter
from transport.keyboards import get_main_menu
import os
import asyncio

class BotRunner:

    def __init__(self, token: str, manager):
        self.bot = Bot(token=token)
        self.dp = Dispatcher()
        self.manager = manager

        self.dp.message.filter(AdminFilter())

        self._register_handlers()


    def _register_handlers(self):
        @self.dp.message(lambda msg: msg.text == "📑 Вкладки")
        async def cmd_tabs(message: types.Message):
            await message.answer("Подглядываю в бразуер 👀")

            result_text = await self.manager.get_all_tabs()

            await message.answer(result_text, parse_mode="HTML")

    
        @self.dp.message(Command("start"))
        async def cmd_start(message: types.Message):
            await message.answer("👋 Привет! Я готов управлять твоим ПК.\nВыбери действие в меню:",
                reply_markup=get_main_menu()
            )

        @self.dp.message(lambda msg: msg.text == "💤 Гибернация")
        async def cmd_hibernate(message: types.Message):
            warning_msg = await message.answer(
                    "⚠️ ПК перейдет в режим гибернации через 3 секунды.\nСохраните все дела!"
            )
            
            try:
                await asyncio.sleep(3)
                await self.manager.hibernate_pc()
                
                try:
                    await message.answer("🌙 Спокойной ночи! ПК выключается...")
                except Exception:
                    pass                     
            except Exception as e:
                await message.answer(f"❌ Ошибка гибернации: {e}")

        
        @self.dp.message(lambda msg: msg.text == "📸 Скриншот")
        async def cmd_hibernate(message: types.Message):
            await message.answer("📸 Заряжаю плёнку...")
            try:
                photo_path = await self.manager.get_screenshot()
                
                photo_file = FSInputFile(photo_path)
                
                await message.answer_photo(
                    photo=photo_file,
                    caption="🖥️ Вот твой скриншот!"
                )
                
                os.remove(photo_path) 
                
            except Exception as e:
                await message.answer(f"❌ Не удалось сделать скриншот: {e}")

    async def start(self):
        print("Бот запущен. Ожидание сообщений от админа...")
        await self.dp.start_polling(self.bot)
