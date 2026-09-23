import asyncio
import time


async def fetch_data(param: int) -> str:
    print(f"Do something with {param}...")
    await time.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"

async def main():

  task1 = asyncio.create_task(fetch_data(1))
  task2 = asyncio.create_task(fetch_data(2))

  print('waiting task1')
  task1_result = await task1
  print('task1 fully completed !!!')

  print('waiting task 2')
  task2_result = await task2
  print('task2 fully completed !!!')

  return [task1_result,task2_result]



if '__name__' == '__main__':
    asyncio.run(main())
