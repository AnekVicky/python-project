import asyncio
import threading 
import os
"""
https://chatgpt.com/g/g-p-6987316154dc8191b6709b6929b4b0a3-python/c/6ab395ac-4d20-83e8-9e23-294cf59eb64f
                Event Loop
                    │
                    ▼
                 main()
                    │
                    ▼
               read_file_async()
                    │
                    ▼
             asyncio.to_thread()
                    │
                    │ submit blocking work
                    ▼
              Thread Pool
                    │
                    ▼
             open() / read()
                    │
                    ▼
                 result
                    │
                    ▼
                Event Loop


                
                
        Event-loop thread
       │
       └── NOT blocked

Worker thread
       │
       └── may block on file I/O
"""
FILE_PATH = '/Users/anekkumarsingh/PycharmProjects/my-app/pythonProject/python-core/docs/lucid/7_time_asyncio.txt'

def read_file_sync(file_path):
    get_thread_info('read_file_sync STARTED')
    with open(file_path,'r') as f:
      return f.read()    ## BLOCKING

def get_thread_info(label):
    print(f'{label}  ,thread name : {threading.current_thread().name} , is_alive :: {threading.current_thread().is_alive()}')

   
# async def read_file_async(file_path):
#  print(f'in read_file_async')
#  return await asyncio.to_thread(read_file_sync,file_path)
   
async def main(file_path):
   print('in main ')
   return await asyncio.to_thread(read_file_sync,file_path)


if __name__ == '__main__':
    content = asyncio.run(main(FILE_PATH))
    print(f'content :: \n\n {content}')

