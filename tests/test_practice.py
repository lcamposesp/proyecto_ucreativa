first_list = ['luis','devops','ucreativa']
second_list = ['devops',1,2]

def test_sublists():
    assert set(first_list()).issubset(get(second_list()))