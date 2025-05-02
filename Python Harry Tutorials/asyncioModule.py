import asyncio
import requests



async def func1():
    url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240226121023/GFG.pdf'
    response = requests.get(url)
    open("gfg.pdf", "wb").write(response.content)
    print("func 1")
    return "Shubham"
    
async def func2():
    url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240226121023/GFG.pdf'
    response = requests.get(url)
    open("gfg2.pdf", "wb").write(response.content)
    print("func 2")
    
async def func3():
    url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240226121023/GFG.pdf'
    response = requests.get(url)
    open("gfg3.pdf", "wb").write(response.content)
    print("func 3")
    
async def main():
    # task = asyncio.create_task(func1())
    # await func2()
    # await func3()
    L = await asyncio.gather(func1(), func2(), func3())
    print(L)
    
asyncio.run(main())