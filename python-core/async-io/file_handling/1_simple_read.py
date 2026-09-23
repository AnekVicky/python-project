

FILE_PATH = '/Users/anekkumarsingh/PycharmProjects/my-app/pythonProject/python-core/docs/lucid/7_time_asyncio.txt'
def main():
    with open(FILE_PATH,'r') as f:
      return f.read()


if __name__ == '__main__':
    content = main()
    print(f'content :: \n\n {content}')