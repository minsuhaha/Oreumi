import time
import functools

def clock(func):
    # functool에서 제공하는 기본 데코레이터
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)  # <--- 함수가 실행
        elasped = time.time() - t0  # <-- 함수가 실행된 총 시간
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(','.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r'%(k,w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elasped, name, arg_str, result))
        return result
    return clocked  

@functools.cache
@clock
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))