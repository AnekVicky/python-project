import asyncio
import os,threading

def get_thread_info(label):
    print(f'{label}  ,thread name : {threading.current_thread().name} , is_alive :: {threading.current_thread().is_alive()}')

def read_files_sync(file_paths :list):
    get_thread_info('read_files_sync STARTED')
    file_result = []
    for file_path in file_paths:
     with open(file_path,'r') as f:
          file_result.append(f.read())
    return file_result

async def main():
    file_paths = [
        '/Users/anekkumarsingh/PycharmProjects/my-app/pythonProject/python-core/docs/lucid/7_time_asyncio.txt',
        '/Users/anekkumarsingh/PycharmProjects/my-app/pythonProject/.gitignore',
        '/Users/anekkumarsingh/PycharmProjects/my-app/pythonProject/README.md'
    ]
    return await asyncio.to_thread(read_files_sync,file_paths) 



if __name__ == '__main__':
    contents = asyncio.run(main())
    for idx,content in enumerate(contents,start=1):
        print(f'file_number :: {idx} ,file_conent : :: {content}')