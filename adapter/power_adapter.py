import asyncio
import os
from subprocess import PIPE

class PowerAdapter:
    def __init__(self):
        self.cmd_hibernate = "systemctl hibernate"

    async def go_hibernate(self):
        try:
            process = await asyncio.create_subprocess_exec(
                "systemctl", "hibernate",
                stdout=PIPE,
                stderr=PIPE
            )
            
            stdout, stderr = await process.communicate()
            
            if process.returncode != 0:
                error_msg = stderr.decode().strip()
                raise RuntimeError(f"Сбой гибернации: {error_msg}")
                
            return True
            
        except FileNotFoundError:
            raise RuntimeError("Команда 'systemctl' не найдена. Проверьте установку systemd.")
        except Exception as e:
            raise RuntimeError(f"Ошибка при выполнении: {e}")

