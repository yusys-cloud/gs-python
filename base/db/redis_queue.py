import os
import redis
import time
import concurrent.futures
import asyncio

redis_client = redis.Redis(host=os.getenv('redis_host'), port=2302) 

llm_req = 'llm_req'

async def my_async_function(delay):
    # 开启Consumer线程        
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        while True:
            dequeue_request()

# Producer 入队
def enqueue_request(request):
    redis_client.rpush(llm_req, str(request))
    print('rpush-->',request)
    
# Consumer 出队    
def dequeue_request():
    data = redis_client.blpop(llm_req, timeout=1)
    if data:
        request = eval(data[1])
        print('Process request', request)
        

        
# 模拟发送请求 
def main():   
    my_async_function(2)      
    for i in range(10):
        request_data = {'id': i, 'input': [0.1, 0.2]}  
        enqueue_request(request_data)
        time.sleep(0.5)


if __name__ == '__main__':  
    main()  