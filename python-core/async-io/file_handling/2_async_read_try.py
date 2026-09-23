import asyncio
"""
Event Loop
    │
    ▼
main()
    │
    ▼
read_file()
    │
    ▼
f.read()  ← BLOCKS
    │
    ▼
return
"""
FILE_PATH = '/Users/anekkumarsingh/PycharmProjects/my-app/pythonProject/python-core/docs/lucid/7_time_asyncio.txt'
async def read_file(file_path):
    print('in read_file')
    with open(file_path,'r') as f:
      return f.read()    ## BLOCKING

async def main(file_path):
   print('in main ')
   return await read_file(file_path = FILE_PATH)
   


if __name__ == '__main__':
    content = asyncio.run(main(FILE_PATH))
    print(f'content :: \n\n {content}')

