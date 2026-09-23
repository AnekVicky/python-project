import asyncio 
import time 

# sync function 
def fetch_data(param :str) -> str :
    print(f'fetching data : {param}')
    time.sleep(param)
    print(f'Done :: {param}')
    return f'fetcted data {param}'


async def main():
    # create and schedule the task on event loop but in a threadpool

    task1_result = await asyncio.create_task( asyncio.to_thread(fetch_data,1) ) 
    task2_result = await asyncio.create_task( asyncio.to_thread(fetch_data,2) ) 
    return [task1_result,task2_result]


if __name__ == '__main__':
    start = time.time()
    result = asyncio.run(main())
    end = time.time()

    print(f'final result :: {result}')
    print(f'process completed in { end - start} secs.')