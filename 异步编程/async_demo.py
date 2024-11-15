# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2024/11/15 16:41
# @FileName  : async_demo.py
# @Author    : Doraemon
import time
# 异步请求
import aiohttp
# 异步处理
import asyncio

def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"执行时间：{(end - start)}s")
        return result
    return wrapper


# 定义协程函数
async def request_async():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.baidu.com") as response:
            print(f"请求结果: {response.status}")
            return response.status


def process_result(future):
    result = future.result()
    print(f"处理结果: {result}")

@calculate_execution_time
def test():
    # 创建异步任务，asyncio.ensure_future：这个函数将一个协程对象包装成一个 Future 对象。Future 是一个表示异步操作最终结果的对象。
    # 适用场景：当你需要显式地管理 Future 对象，或者在某些情况下需要立即调度这些任务时，可以使用这种方式。
    # 这样可以直接在事件循环中使用这些 Future 对象
    tasks = [asyncio.ensure_future(request_async()) for i in range(0, 49)]
    # 每个任务执行完成后会调用回调函数
    for task in tasks:
        # 添加回调函数
        task.add_done_callback(process_result)
    # 直接生成协程对象
    # tasks = [request_async() for i in range(0, 49)]
    # 获取当前事件循环，事件循环是异步编程的核心组件，负责管理和调度协程、任务和回调函数的执行
    # 返回当前线程的事件循环。如果没有事件循环在运行，则会创建一个新的事件循环。
    loop = asyncio.get_event_loop()
    # 将所有任务打包成一个任务组
    tasks = asyncio.gather(*tasks)
    # 运行事件循环直到所有的任务完成
    loop.run_until_complete(tasks)
    # 关闭事件循环
    loop.close()

test()