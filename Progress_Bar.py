import asyncio
import os

Loop = asyncio.get_event_loop()

async def Preview(Length):
    def Render(Countdown):
        os.system("cls||clear")
        print(f"Countdowm in {Length - Countdown}")
        print(f"[{''.join(Progress)}]")
    Progress = ["🟥" for i in range(Length)]
    Render(0)
    for i in range(1, Length + 1):
        Progress[i - 1] = "🟩"
        await asyncio.sleep(1)
        Render(i)
    await asyncio.sleep(1)
    os.system("cls||clear")

Loop.run_until_complete(Preview(100))