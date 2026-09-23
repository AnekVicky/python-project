import asyncio
import time

# https://lucid.app/lucidchart/580760be-b7bc-40bc-80a3-cba7b3352190/edit?page=page1&invitationId=inv_0c0e6f42-cee2-4ca6-aa85-d2e3c87c5ed8#

"""
  Important Concept : 
  --------------------------------------------------------------
  |task 2 coroutine -> |task 1 coroutine -> | main coroutine |          FIFO this FIFO is ready queue of FIFO NOT the coroutine execution order.
  --------------------------------------------------------------
see the program print statement after run .
 
  once task1 is done means await task1 is done then control goes to event loop and since task2 is already scheduled & in ready status
  event loop will pick task2 and run it. So task2 will be executed after task1 is done NOT main coroutine. 
  So main coroutine will be in waiting state until task2 is done.

"""


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
