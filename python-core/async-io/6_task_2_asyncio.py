import asyncio


async def fetch_data(param: int) -> str:
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))

    task2_result = await task2
    print("Task 2 fully completed")

    task1_result = await task1
    print("Task 1 fully completed")
    return [task1_result, task2_result]


if __name__ == '__main__':
    final_result = asyncio.run(main())
    print(final_result)

