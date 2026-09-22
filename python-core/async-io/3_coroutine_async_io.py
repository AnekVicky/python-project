import asyncio
import time


async def async_function(param: str) -> str:
    print(f'async_function enter :: {param}')
    await asyncio.sleep(5)
    return f'async_function returned : {param}'


async def main():
    coroutine_obj = async_function("test_param")
    print(f'coroutine obj :: {coroutine_obj}')

    coroutine_result = await coroutine_obj
    print(coroutine_result)

if __name__ == '__main__':
    asyncio.run(main())

