import asyncio
import time
async def main():
    print("enter async main")
    await asyncio.sleep(5)
    print("exit async main")

    return f"returned from async function"

if __name__ == '__main__':
    result = asyncio.run(main())
    print(result)

