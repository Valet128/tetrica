
def strict(func):
    def wrap(*args, **kwargs):
        for i, v in enumerate(func.__annotations__.values()):
            if func.__defaults__:
                raise ValueError("Функция не может содержать параметры по умолчанию")
            if i + 1 == len(func.__annotations__):
                break
            if type(args[i]) not in (bool, int, str, float):
                raise TypeError("Параметры такого типа не поддерживаются данной функцией")
            if not isinstance(args[i], v):
                raise TypeError("Параметры не соответствуют аннотации")
            

        result=func(*args, **kwargs)
        return result
    
    return wrap


def sum_two(a: int , b: int) -> int:
    return a + b


print(sum_two(1, False))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
