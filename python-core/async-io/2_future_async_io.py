import asyncio
import time
async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    print(f"Empty future {future}")

    future.set_result("Future result test")
    future_result = await future
    print(f'future result :: {future_result}')

if __name__ == '__main__':
    asyncio.run(main())

