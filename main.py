import asyncio
from config import config
from adapter.browser_adapter import BrowserAdapter
from adapter.screen_adapter import ScreenAdapter
from adapter.power_adapter import PowerAdapter
from manager.pc_manager import PCManager
from transport.bot import BotRunner

async def main():
    browser_adapter = BrowserAdapter()
    screen_adapter = ScreenAdapter()
    power_adapter = PowerAdapter()

    pc_manager = PCManager(browser_adapter=browser_adapter, screen_adapter=screen_adapter, power_adapter=power_adapter)
    
    bot_runner = BotRunner(token=config.TOKEN, manager=pc_manager)

    print("Bot running..")
    await bot_runner.start()


if __name__ == "__main__":
    asyncio.run(main())
