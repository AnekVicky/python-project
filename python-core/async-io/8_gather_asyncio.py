import asyncio
import time


async def download_file(param:str) -> str:
    print(f"Downloading file : {param}")
    await asyncio.sleep(3)
    return f"Downloaded file : {param}"


async def main():
   tasks = await asyncio.gather(download_file("file1"), 
                                download_file("file2"), 
                                download_file("file3"))
   return tasks
 

if __name__ == '__main__':
    start_time = time.perf_counter()

    final_result = asyncio.run(main())

    end_time = time.perf_counter()
    print(final_result)
    print(f"Total time taken : {end_time - start_time} seconds")

    