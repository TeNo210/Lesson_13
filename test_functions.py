from functions import salary,hello_who
def test_hello_who_max():
    assert hello_who('Max') =='Hello, Max'
    assert hello_who('Alex') == 'Hello, Alex'
    assert hello_who('Tosha') == 'Hello, Tosha'
    assert hello_who('Jax') == 'Hello, Jax'
    assert hello_who('Kolya') == 'Hello, Kolya'

def test_salary():
    assert (2, 2) != 8
    assert (3, 1) != 6