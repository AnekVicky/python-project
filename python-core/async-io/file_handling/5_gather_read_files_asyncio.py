import asyncio
import os,threading


"""
                    Event Loop
                        │
              ┌─────────┼─────────┐
              │         │         │
              ▼         ▼         ▼
           Task 1    Task 2    Task 3
              │         │         │
              ▼         ▼         ▼
          asyncio_0  asyncio_1  asyncio_2
              │         │         │
              ▼         ▼         ▼
           file 1     file 2     file 3
              │         │         │
              └─────────┼─────────┘
                        ▼
                 asyncio.gather()
                        │
                        ▼
                     results
"""

def get_thread_info(label):
    print(f'{label}  ,thread name : {threading.current_thread().name} , is_alive :: {threading.current_thread().is_alive()}')

def read_files_sync(file_path):
    get_thread_info('read_files_sync STARTED')
    with open(file_path,'r') as f:
        return  f.read()


async def main():
    file_paths = [
        '/Users/anekkumarsingh/PycharmProjects/my-app/pythonProject/python-core/docs/lucid/7_time_asyncio.txt',
        '/Users/anekkumarsingh/PycharmProjects/my-app/pythonProject/.gitignore',
        '/Users/anekkumarsingh/PycharmProjects/my-app/pythonProject/README.md'
    ]
    tasks = [asyncio.to_thread(read_files_sync,file_path) for file_path in file_paths]

    return await asyncio.gather(*tasks)



if __name__ == '__main__':
    contents = asyncio.run(main())
    for idx,content in enumerate(contents,start=1):
        print(f'file_number :: {idx} ,file_conent : :: {content}')