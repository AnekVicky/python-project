import asyncio


"""
                  EVENT LOOP
                       │
                       ▼
                 ┌───────────┐
                 │ Producer  │
                 └─────┬─────┘
                       │
                 put(file)
                       │
                       ▼
              ┌────────────────┐
              │ Queue(max=20)  │
              └────────────────┘
                 │ │ │ │ │
                 ▼ ▼ ▼ ▼ ▼
                C1 C2 C3 C4 C5
                 │ │ │ │ │
                 │ │ │ │ │ await
                 │ │ │ │ │
                 ▼ ▼ ▼ ▼ ▼
              to_thread()
                 │ │ │ │ │
                 ▼ ▼ ▼ ▼ ▼
              Thread Pool
                 │ │ │ │ │
                 ▼ ▼ ▼ ▼ ▼
              File System
                 │
                 ▼
             file processed
                 │
                 ▼
            task_done()

"""

def read_file_sync(file_path):
    print('read_files_sync STARTED')
    with open(file_path,'r') as f:
        return  f.read()

async def producer(queue):

    for i in range(100):
        await queue.put(f"file{i}.txt")

    for _ in range(5):
        await queue.put(None)


async def consumer(queue):

    while True:
        filename = await queue.get()

        if filename is None:
            queue.task_done()
            break
        try:
            content = await asyncio.to_thread(read_file_sync,filename)
            print(f"Processed {filename}")

        finally:
            queue.task_done()

async def main():

    queue = asyncio.Queue(maxsize=20)

    async with asyncio.TaskGroup() as tg:

        consumers = [
            tg.create_task(consumer(queue))
            for _ in range(5)
        ]

        producer_task = tg.create_task(
            producer(queue)
        )

        # Wait for producer to finish producing
        await producer_task

        # Now no more real work will be added.
        # Wait until consumers process everything.
        await queue.join()

        # Stop consumers
        for _ in range(5):
            await queue.put(None)