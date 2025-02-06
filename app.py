import redis
r = redis.Redis(host="localhost", port=6379, decode_responses=True)


def print_cache():
    keys = r.keys("*")
    for key in keys:
        value = r.get(key)
        print(f"{key}: {value}")


def fib_recursive(num):
    if num <= 1:
        return num
    if cached_result := r.get(str(num)):
        return int(cached_result)
    result = fib_recursive(num - 1) + fib_recursive(num - 2)
    r.set(str(num), result)
    return result


if __name__ == "__main__":
    print(fib_recursive(1000))
    print_cache()
    # r.flushdb()
