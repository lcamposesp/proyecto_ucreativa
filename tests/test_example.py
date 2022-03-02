def sum_fun(x,y):
    return x+y

def rest_fun(x,y):
    return x-y

def test_sum():
    assert sum_fun(10,11) > 5 

def test_rest():
    assert rest_fun(10,11) == 1