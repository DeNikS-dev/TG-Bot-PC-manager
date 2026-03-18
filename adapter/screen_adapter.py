from PIL import ImageGrab
import asyncio
import os
from pathlib import Path

class ScreenAdapter:
    def __init__(self):
        self.temp_dir = Path("/tmp")
        self.filename = "pc_bot_screenshot.png"
        self.file_path = f"{self.temp_dir}/{self.filename}"

    async def take_screenshot(self) -> str:

        screenshot = ImageGrab.grab()
        screenshot.save(self.file_path)

        chk_file_pth = Path(self.file_path)
        if chk_file_pth.exists() == False:
            raise FileNotFoundError("Файл скриншота не был создан или пуст.")

        return str(self.file_path)
