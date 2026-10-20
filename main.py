from connection import *
from service import *
import asyncio


async def main():
    await create_table()
    while True:
        n=int(input("1)Create task\n2)Get task\n0)Exit\nChouse one: "))
        match n:
            case 1:
                await create_task(input("Title: "), input("Description: "), input("Dueration date: "))
            case 2:
                await get_task()
            case 0:
                break
            case _:
                print("invalid input")
                
if __name__ == "__main__":
    asyncio.run(main())

                
