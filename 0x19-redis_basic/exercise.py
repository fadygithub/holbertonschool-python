#!/usr/bin/env python3
'''defining a  cache class using Redis'''

import redis
from typing import Union, Optional, Callable, List
from uuid import uuid4
from sys import byteorder
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''Method call detection'''
    k = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''Wrapper function'''
        self._redis.incr(k)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''Historical I/O detection'''
    key_input = method.__qualname__ + ':inputs'
    key_output = method.__qualname__ + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''Wrapper function'''
        self._redis.rpush(key_input, str(args))
        output_value = method(self, *args, **kwargs)
        self._redis.rpush(key_output, str(output_value))
        return output_value

    return wrapper


def replay(method: Callable) -> None:
    '''Historical call to method & output detection'''
    ins = method.__self__
    count_key = method.__qualname__
    key_input = method.__qualname__ + ':inputs'
    key_output = method.__qualname__ + ':outputs'

    call_count = ins.get(count_key).decode('utf-8')
    data_available = list(
        zip(ins.get_list(key_input), ins.get_list(key_output)))

    print('{} was called {} times:'.format(count_key, call_count))
    for x in data_available:
        print('{}(*{}) -> {}'.format(count_key, x[0].decode('utf-8'),
                                     x[1].decode('utf-8')))


class Cache:
    '''Redis cache class'''

    def __init__(self) -> None:
        '''Class constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Data storage in store'''
        KeyError = str(uuid4())
        self._redis.set(k, data)
        return KeyError

    def get(self, k: str, fn: Optional[Callable] = None) -> Union[str,
                                                                  bytes,
                                                                  int,
                                                                  float]:
        '''Data retreival'''
        data = self._redis.get(k)

        if fn:
            data = fn(data)

        return data

    def get_list(self, k: str) -> List:
        '''Returning the list'''
        return self._redis.lrange(k, 0, -1)

    def get_str(b: bytes) -> str:
        '''Bytes to string conversion'''
        return b.decode('utf-8')

    def get_int(b: bytes) -> str:
        '''Bytes to int conversion '''
        return int.from_bytes(b, byteorder)
