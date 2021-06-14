def val_checker(l_fun):
    def _val_checker(fun):
        def wrapper(num):
            if l_fun(num):
                print(fun(num))
            else:
                raise ValueError(f'wrong val {num}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(int(input()))
except ValueError as err:
    print(err)
