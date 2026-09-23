import asyncio
import time


async def async_function(param: str) -> str:
    print(f'async_function enter :: {param}')
    await asyncio.sleep(5)
    return f'async_function returned : {param}'


async def main():
    task = asyncio.create_task(async_function("test_param")) #it creates and schedules the task in the event loop
    print(f'task obj :: {task}')

    task_result = await task
    print(task_result)

if __name__ == '__main__':
    asyncio.run(main())

