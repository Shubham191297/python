import multiprocessing
import requests
from concurrent.futures import ProcessPoolExecutor

def downloadFile(url, name):
    print("Started downloading...")
    response = requests.get(url)
    open(f"files/file{name}.jpg","wb").write(response.content)
    print("Finished downloading...")
    
urls = [
    "https://images.unsplash.com/photo-1726137569820-bff1c68311a1?q=80&w=3687&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1745552383962-c555a920229c?q=80&w=3575&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1745905506748-1c86cfd006a1?q=80&w=3687&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1745428847642-34364849140e?q=80&w=2533&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
]

# This was using simple code
# pros = []
# if __name__ == '__main__': 
#     for i,url in enumerate(urls):
#         # downloadFile(url,i) 
#         p = multiprocessing.Process(target=downloadFile,args=[url,i])
#         p.start()
#         pros.append(p)
        
#     for p in pros:
#         p.join()


# This was using process pool executor
if __name__=='__main__':
    with ProcessPoolExecutor() as executor:
        num = [0,1,2,3]
        results=executor.map(downloadFile,urls,num)
        for r in results:
            print(r)