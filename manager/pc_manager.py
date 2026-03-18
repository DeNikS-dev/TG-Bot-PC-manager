from adapter.browser_adapter import BrowserAdapter 
from adapter.screen_adapter import ScreenAdapter
from adapter.power_adapter import PowerAdapter

class PCManager:
    def __init__(self, browser_adapter: BrowserAdapter, screen_adapter: ScreenAdapter, power_adapter: PowerAdapter):
        self.browser_adapter = browser_adapter
        self.screen_adapter = screen_adapter
        self.power_adapter = power_adapter


    async def get_all_tabs(self):
        try:
            tabs_data = await self.browser_adapter.get_tabs()

            if len(tabs_data) == 0:
                return "Вкладок нету =("
            
            message = "📑 <b>Открытые вкладки:</b>\n\n"
            
            for i, tab in enumerate(tabs_data, 1):
                title = tab.get('title', 'Без названия')
                url = tab.get('url', '')
                
                if len(title) > 50:
                    title = title[:47] + "..."
                
                message += f"{i}. <a href='{url}'>{title}</a>\n"
            
            return message

        except Exception as e:
            print(f"Error: {e}")
            return f"Ошибка: {e}"

    async def get_screenshot(self):
        try:
            file_path = await self.screen_adapter.take_screenshot()
            return file_path
        except Exception as e:
            print(f"Error: {e}")
            return f"Ошибка: {e}"


    async def hibernate_pc(self):
        await self.power_adapter.go_hibernate()
        return True
