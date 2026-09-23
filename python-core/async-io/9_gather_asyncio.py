import asyncio
import time


async def download_file(param:str) -> str:
    print(f"Downloading file : {param}")
    await asyncio.sleep(1)
    return f"Downloaded file : {param}"


async def main():
   tasks = [download_file(str(i)) for i in range(1,5)]
   result = await asyncio.gather(*tasks)
   return result
 

if __name__ == '__main__':
    start_time = time.time()

    final_result = asyncio.run(main())

    end_time = time.time()
    print(final_result)
    print(f"Total time taken : {end_time - start_time} seconds")

    