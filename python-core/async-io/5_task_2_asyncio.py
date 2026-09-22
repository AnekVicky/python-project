import asyncio


async def fetch_data(param: int) -> str:
    print(f"Do something : {param}")
    await asyncio.sleep(3)
    print(f"Done : {param}")


async def main():
    task1 = asyncio.create_task(fetch_data(1))  # creates task and schedules it with event loop immediately
    task2 = asyncio.create_task(fetch_data(2))  # creates task and schedules it with event loop immediately

    print("await 2 ....")
    task1_result = await task2
    print("task2 fully completed.")

    print("await 1 .....")
    task2_result = await task1
    print("task1 fully completed.")
    return [task1_result,task2_result]


if __name__ == '__main__':
    final_result = asyncio.run(main())
    print(final_result)