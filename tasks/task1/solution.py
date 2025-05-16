from functools import wraps


def strict(func):
    @wraps(func)
    def inner(*args, **kwargs):

        kwargs_attrs = dict(func.__annotations__)
        args_attrs = list(kwargs_attrs.values())

        if args:
            for arg_id in range(len(args)):
                if type(args[arg_id]) is not args_attrs[arg_id]:
                    raise TypeError("Wrong attr type")

        if kwargs:
            for k in kwargs.keys():
                if type(kwargs[k]) is not kwargs_attrs[k]:
                    raise TypeError("Wrong attr type")

        result = func(*args, **kwargs)
        return result

    return inner


@strict
def sum_two(a: int, b: int) -> int:
    return a + b
