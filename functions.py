def func1(an_arg, a_func):
    def func2(another_arg):
        return another_arg * 2
    
    value = func2(an_arg)
    return a_func(value)

an_arg = 1

def any_func(any_value):
    return any_value + 5

func1(an_arg, any_func)