import asyncio
"""
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
"""
FILE_PATH = '/Users/anekkumarsingh/PycharmProjects/my-app/pythonProject/python-core/docs/lucid/7_time_asyncio.txt'
def read_file_sync(file_path):
    print('in read_file')
    with open(file_path,'r') as f:
      return f.read()    ## BLOCKING


async def read_file_async(file_path):
 print(f'in read_file_async')
 return await asyncio.to_thread(read_file_sync,file_path)
   
async def main(file_path):
   print('in main ')
   return await read_file_async(file_path = FILE_PATH)
   


if __name__ == '__main__':
    content = asyncio.run(main(FILE_PATH))
    print(f'content :: \n\n {content}')

