import aiohttp
import json
from config import config

class BrowserAdapter:
    def __init__(self):
        self.base_url = config.URL
        self.bot_token = config.TOKEN

    async def get_tabs(self):
        """
        Асинхронный метод получения списка вкладок браузера 
        """
        result_json = []
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url) as response:

                data = await response.json()
                for tab in data:
                    if tab.get('type') == "page":
                        clean_tab = {
                            "title": tab.get('title', 'Без названия'),
                            "url": tab.get('url', '')
                        }
                        
                        result_json.append(clean_tab)
                        
                        # print(f"Found tab: {json.dumps(clean_tab)}")



        return result_json
        


