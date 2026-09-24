import asyncio
import os,threading


"""
What is the problem with the code ?
Here asyncio.to_thread is being awaited sequentially  ,hence in o/p ,you will see one thread running at a time .

sol:  use gather
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
    return [await asyncio.to_thread(read_files_sync,file_path) for file_path in file_paths]



if __name__ == '__main__':
    contents = asyncio.run(main())
    for idx,content in enumerate(contents,start=1):
        print(f'file_number :: {idx} ,file_conent : :: {content}')